state.originalAuthorsNote = "[Phase:{{phase}}] [Style:{{style}}] [Directive:{{directive}}] [Faction:{{faction}}] [Terrain:{{terrain}}] [Context:{{context}}]";
state.authorsNoteLockDuration = 2;

state.initialHeat = 0;
state.initialInstability = 1;
state.instabilityIncreaseChance = 15;
state.heatIncreaseValue = 1;
state.instabilityIncreaseValue = 1;

state.playerHeatImpact = 2;
state.playerInstabilityImpact = 1;
state.modelHeatImpact = 1;
state.modelInstabilityImpact = 1;

state.maxInstability = 16;
state.trueMaxInstability = 21;
state.minInstability = 1;
state.trueMinInstability = 1;

state.cooldownTimer = 5;
state.cooldownRate = 2;
state.overloadTimer = 4;
state.overloadHeatReduction = 5;
state.overloadInstabilityReduction = 1;

state.randomSurgeChance = 3;
state.randomSurgeHeat = 5;
state.randomSurgeInstability = 2;

const factions = {
  "Order": ["structure", "law", "enforce", "stability", "cohesion", "guard", "preserve"],
  "Wilds": ["improvise", "chaos", "collapse", "salvage", "repurpose", "nomad", "refuse"],
  "Conflux": ["mediate", "balance", "translate", "negotiate", "observe", "signal"]
};

const terrain = {
  "Ruins": ["crumble", "debris", "fragment", "threshold", "residue", "collapse"],
  "Settlements": ["town", "road", "outpost", "camp", "structure", "enclave"],
  "Wildlands": ["gorge", "waste", "ridge", "overgrowth", "abandoned", "unstable"]
};

const salvageLogic = {
  "lift": ["learn", "repurpose", "adapt", "signal", "extract", "salvage"],
  "drop": ["memory", "loss", "ruin", "fragment", "residue", "forgotten"],
  "shear": ["rupture", "unstable", "collapse", "threshold", "break", "shatter"],
  "invert": ["contradiction", "betrayal", "reversal", "refuse", "usurp", "replace"]
};
function scoreText(text, words) {
  const lower = text.toLowerCase();
  return words.reduce((score, word) => lower.includes(word) ? score + 1 : score, 0);
}

function getRankedTone(text, dictionary) {
  const scores = Object.entries(dictionary)
    .map(([key, words]) => ({ key, score: scoreText(text, words) }))
    .filter(item => item.score > 0)
    .sort((a, b) => b.score - a.score);
  if (scores.length === 0) return "None";
  return `${scores[0].key}(P)` + (scores[1] ? `,${scores[1].key}(S)` : "");
}
const fracturedModifier = (text) => {
  const isPlayerTurn = typeof info !== 'undefined' && info.actionType === 'input';

  if (state.heat === undefined) {
    state.heat = state.initialHeat;
    state.instability = state.initialInstability;
    state.cooldownMode = false;
    state.overloadMode = false;
    state.currentLocation = "Twisting-Gorge";
    state.authorsNoteLockCounter = 0;
    state.lockedAuthorsNote = "";
  }

  const factionTone = getRankedTone(text, factions);
  const terrainTone = getRankedTone(text, terrain);
  const salvageTone = getRankedTone(text, salvageLogic);

  const conflictScore = scoreText(text, salvageLogic.shear) + scoreText(text, factions.Wilds);
  const calmScore = scoreText(text, factions.Order);

  if (!state.cooldownMode) {
    if (conflictScore > 0) {
      state.heat += conflictScore * state.playerHeatImpact;
      if (conflictScore >= 2) state.instability += state.playerInstabilityImpact;
    }
    if (calmScore > 0) {
      state.heat -= calmScore * state.modelHeatImpact;
      if (calmScore >= 2) state.instability -= state.modelInstabilityImpact;
    }
  }

  if (randomint(1, 100) <= state.randomSurgeChance) {
    if (salvageTone.includes("shear")) {
      state.heat += 8;
      state.instability += 3;
    } else if (salvageTone.includes("drop")) {
      state.heat += 5;
      state.instability += 2;
    } else {
      state.heat += state.randomSurgeHeat;
      state.instability += state.randomSurgeInstability;
    }
  }

  if (!state.cooldownMode && !state.overloadMode) state.heat += state.heatIncreaseValue;
  if (randomint(1, state.instabilityIncreaseChance) <= state.heat) {
    state.heat = 0;
    state.instability += state.instabilityIncreaseValue;
  }

  if (state.instability >= state.maxInstability && !state.cooldownMode && !state.overloadMode) {
    state.overloadMode = true;
    state.overloadTurnsLeft = state.overloadTimer;
  }

  if (state.cooldownMode) {
    state.cooldownTurnsLeft--;
    state.instability -= state.cooldownRate;
    if (state.cooldownTurnsLeft <= 0) state.cooldownMode = false;
  } else if (state.overloadMode) {
    state.overloadTurnsLeft--;
    if (state.overloadTurnsLeft <= 0) {
      state.instability -= state.overloadInstabilityReduction;
      state.heat -= state.overloadHeatReduction;
      state.overloadMode = false;
      state.cooldownMode = true;
      state.cooldownTurnsLeft = state.cooldownTimer;
    }
  }

  state.instability = Math.max(state.trueMinInstability, Math.min(state.instability, state.trueMaxInstability));
  let phase = ""; let directive = ""; let style = ""; let context = "";

  if (state.instability <= 2) {
    phase = "Orientation. Introduce terrain, factions, and thresholds. No conflict unless initiated.";
    directive = "Focus on environmental storytelling and faction presence.";
    style = "Ambient tension, grounded tone.";
  } else if (state.instability <= 8) {
    phase = "Rising Pressure. Introduce salvage opportunities, faction tension, and unstable terrain.";
    directive = "Repurpose debris and signal consequences.";
    style = "Improvisational, consequence-driven.";
  } else if (state.instability <= 15) {
    phase = "Climax. Faction conflict peaks. Terrain fractures. Salvage becomes volatile.";
    directive = "Push players toward irreversible choices.";
    style = "High tension, grounded realism.";
  } else {
    phase = "Collapse. No resolution. Terrain fails. Factions splinter.";
    directive = "Hold chaos. Refuse closure.";
    style = "Unstable, refusal-based.";
  }

  context = `Loc:${state.currentLocation}. Faction:${factionTone}. Terrain:${terrainTone}. Salvage:${salvageTone}.`;

  let tempNote = state.originalAuthorsNote;
  tempNote = tempNote.replace("{{phase}}", phase)
                     .replace("{{directive}}", directive)
                     .replace("{{style}}", style)
                     .replace("{{faction}}", factionTone)
                     .replace("{{terrain}}", terrainTone)
                     .replace("{{context}}", context);

  state.memory.authorsNote = tempNote;

  if (isPlayerTurn) {
    state.lockedAuthorsNote = state.memory.authorsNote;
    state.authorsNoteLockCounter = state.authorsNoteLockDuration;
  }

  return { text };
};
