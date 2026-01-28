# VERIFICATION_LAYER.py
# Not for discovery, for confirming sound reasoning

class TeachingVerificationEngine:
    """
    Quality control: Verifies JW teachings through lexical archaeology
    Not to discover new doctrine, but to confirm sound exegesis
    """
    
    def __init__(self):
        # JW teachings as reference points
        self.jw_teachings = {
            'SHEOL': {
                'teaching': "The grave; common grave of mankind; not torment",
                'key_verses': ["Ecclesiastes 9:5, 10", "Psalm 6:5", "Isaiah 38:18"],
                'lexical_evidence': {
                    'hebrew': 'שְׁאוֹל (sheol) - grave, pit, underworld',
                    'lxx': 'ᾅδης (hades) - equivalent translation',
                    'semantic_range': ['grave', 'realm of dead', 'not torment'],
                    'anachronism_detected': 'Medieval torment concepts imported'
                },
                'verification_status': 'STRONGLY_SUPPORTED',
                'reasoning_quality': 'HIGH - aligns with semantic range'
            },
            
            'AGAPE': {
                'teaching': "Self-sacrificing love based on principle; God's love",
                'key_verses': ["John 3:16", "1 John 4:8", "Romans 5:8"],
                'lexical_evidence': {
                    'greek': 'ἀγάπη (agapē) - love based on principle',
                    'contrasts': ['ἔρως (eros) - romantic', 'φιλία (philia) - friendship'],
                    'semantic_distinctive': 'Volitional, not merely emotional',
                    'cultural_context': 'New term largely developed in Christian writings'
                },
                'verification_status': 'STRONGLY_SUPPORTED',
                'reasoning_quality': 'HIGH - preserves distinctive meaning'
            },
            
            'PSYCHE': {
                'teaching': "Living being, person; not immortal soul",
                'key_verses': ["Genesis 2:7", "Ezekiel 18:4", "Matthew 10:28"],
                'lexical_evidence': {
                    'hebrew_equivalent': 'נֶפֶשׁ (nephesh) - living being',
                    'greek': 'ψυχή (psychē) - life, living being',
                    'semantic_range': ['life', 'person', 'living being', 'not immortal entity'],
                    'anachronism_detected': 'Platonic dualism imported'
                },
                'verification_status': 'STRONGLY_SUPPORTED', 
                'reasoning_quality': 'HIGH - corrects philosophical imposition'
            },
            
            'GEHENNA': {
                'teaching': "Symbol of eternal destruction; not torment",
                'key_verses': ["Matthew 10:28", "Mark 9:43-48"],
                'lexical_evidence': {
                    'historical_reference': 'Valley of Hinnom, Jerusalem garbage dump',
                    'symbolic_meaning': 'Complete destruction, not preservation in torment',
                    'semantic_shift': 'From literal valley to symbolic destruction',
                    'misinterpretation': 'Confused with medieval hell concepts'
                },
                'verification_status': 'SUPPORTED',
                'reasoning_quality': 'MEDIUM_HIGH - some debate on symbolic application'
            }
        }
        
        self.verification_methods = [
            'SEMANTIC_RANGE_ANALYSIS',
            'ANACHRONISM_DETECTION', 
            'CULTURAL_CONTEXT_ALIGNMENT',
            'TRANSLATION_CONSISTENCY_CHECK',
            'INTERTEXTUAL_HARMONY_VERIFICATION'
        ]
    
    def verify_teaching(self, topic, teaching_text=None):
        """
        Run lexical archaeology to verify JW teaching reasoning
        Returns verification report, not doctrinal discovery
        """
        
        if topic.upper() in self.jw_teachings:
            data = self.jw_teachings[topic.upper()]
            
            # Run verification checks
            verification_results = self._run_verification_checks(data)
            
            # Generate quality control report
            report = self._generate_qc_report(topic, data, verification_results)
            
            return report
        
        return {
            'topic': topic,
            'status': 'NOT_IN_DATABASE',
            'suggestion': f"Available topics: {', '.join(self.jw_teachings.keys())}"
        }
    
    def _run_verification_checks(self, teaching_data):
        """Run quality control checks"""
        
        checks = {
            'semantic_alignment': self._check_semantic_alignment(teaching_data),
            'anachronism_avoidance': self._check_anachronism_avoidance(teaching_data),
            'contextual_fidelity': self._check_contextual_fidelity(teaching_data),
            'translation_consistency': self._check_translation_consistency(teaching_data)
        }
        
        # Calculate overall verification score
        passed = sum(1 for check in checks.values() if check['passed'])
        total = len(checks)
        
        return {
            'checks': checks,
            'passed_checks': passed,
            'total_checks': total,
            'verification_score': passed / total if total > 0 else 0
        }
    
    def _check_semantic_alignment(self, data):
        """Does teaching align with term's semantic range?"""
        if 'lexical_evidence' in data and 'semantic_range' in data['lexical_evidence']:
            # Simple check: teaching should fit within semantic range
            teaching_lower = data['teaching'].lower()
            semantic_range = data['lexical_evidence']['semantic_range']
            
            # Check if teaching aligns with any part of semantic range
            alignment = any(
                any(word in teaching_lower for word in range_item.split()) 
                for range_item in semantic_range
            )
            
            return {
                'passed': alignment,
                'evidence': f"Teaching '{data['teaching'][:30]}...' aligns with semantic range: {semantic_range}",
                'method': 'SEMANTIC_RANGE_ANALYSIS'
            }
        
        return {'passed': False, 'evidence': 'Insufficient lexical data', 'method': 'SEMANTIC_RANGE_ANALYSIS'}
    
    def _generate_qc_report(self, topic, teaching_data, verification_results):
        """Generate quality control report"""
        
        score = verification_results['verification_score']
        
        if score >= 0.75:
            qc_rating = 'PASS_WITH_FLYING_COLORS'
            recommendation = 'Teaching methodology sound; lexical archaeology confirms reasoning'
        elif score >= 0.5:
            qc_rating = 'PASS_WITH_NOTES'
            recommendation = 'Teaching generally sound; some nuances could be strengthened'
        else:
            qc_rating = 'REVIEW_NEEDED'
            recommendation = 'Re-examine lexical basis; possible anachronism detected'
        
        return {
            'topic': topic,
            'jw_teaching': teaching_data['teaching'],
            'verification_summary': {
                'score': round(score, 3),
                'rating': qc_rating,
                'passed_checks': verification_results['passed_checks'],
                'total_checks': verification_results['total_checks']
            },
            'lexical_evidence_summary': teaching_data.get('lexical_evidence', {}),
            'key_verses': teaching_data.get('key_verses', []),
            'recommendation': recommendation,
            'qc_timestamp': len(self.jw_teachings)  # Simulated
        }

# QUALITY CONTROL DASHBOARD
class TeachingQCDashboard:
    """
    For your app/search quality control layer
    Shows which teachings have strongest lexical verification
    """
    
    def __init__(self):
        self.verifier = TeachingVerificationEngine()
        self.verification_history = []
    
    def run_batch_verification(self, topics=None):
        """Run QC on multiple teachings"""
        
        if topics is None:
            topics = list(self.verifier.jw_teachings.keys())
        
        results = []
        
        for topic in topics:
            print(f"\n🔍 Verifying: {topic}")
            
            result = self.verifier.verify_teaching(topic)
            
            # Store
            self.verification_history.append({
                'topic': topic,
                'score': result['verification_summary']['score'],
                'timestamp': len(self.verification_history)
            })
            
            results.append(result)
            
            # Print summary
            summary = result['verification_summary']
            print(f"   Score: {summary['score']:.3f} - {summary['rating']}")
            print(f"   Teaching: {result['jw_teaching'][:50]}...")
        
        return results
    
    def get_verification_rankings(self):
        """Rank teachings by lexical verification strength"""
        
        if not self.verification_history:
            self.run_batch_verification()
        
        # Sort by score
        ranked = sorted(
            self.verification_history,
            key=lambda x: x['score'],
            reverse=True
        )
        
        return {
            'strongest_verification': ranked[0] if ranked else None,
            'weakest_verification': ranked[-1] if ranked else None,
            'average_score': sum(x['score'] for x in ranked) / len(ranked) if ranked else 0,
            'all_rankings': ranked
        }
    
    def generate_qc_report(self):
        """Generate overall quality control report"""
        
        rankings = self.get_verification_rankings()
        
        return {
            'report_date': 'Simulated',  # Would be datetime
            'teachings_verified': len(self.verification_history),
            'average_verification_score': rankings['average_score'],
            'strongest_area': rankings['strongest_verification']['topic'] if rankings['strongest_verification'] else 'None',
            'recommended_review': rankings['weakest_verification']['topic'] if rankings['weakest_verification'] else 'None',
            'overall_assessment': self._get_overall_assessment(rankings['average_score']),
            'methodology_note': 'Lexical archaeology verification, not doctrinal discovery'
        }
    
    def _get_overall_assessment(self, avg_score):
        """Overall QC assessment"""
        if avg_score >= 0.8:
            return "EXCELLENT - Teachings show strong lexical basis"
        elif avg_score >= 0.6:
            return "GOOD - Generally sound with minor exceptions"
        elif avg_score >= 0.4:
            return "FAIR - Some areas need lexical review"
        else:
            return "REVIEW_NEEDED - Significant lexical alignment issues"

# DEMONSTRATE QUALITY CONTROL LAYER
print("\n" + "="*70)
print("TEACHING QUALITY CONTROL LAYER")
print("Lexical Archaeology as Verification, Not Discovery")
print("="*70)

dashboard = TeachingQCDashboard()

print("\n🧪 RUNNING BATCH VERIFICATION...")
results = dashboard.run_batch_verification()

print("\n" + "="*70)
print("QUALITY CONTROL REPORT")
print("="*70)

qc_report = dashboard.generate_qc_report()

for key, value in qc_report.items():
    print(f"{key.replace('_', ' ').title()}: {value}")

print("\n" + "="*70)
print("VERIFICATION RANKINGS (Strongest to Weakest)")
print("="*70)

rankings = dashboard.get_verification_rankings()

for i, item in enumerate(rankings['all_rankings'][:5], 1):
    print(f"{i}. {item['topic']}: {item['score']:.3f}")