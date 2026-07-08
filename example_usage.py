"""
example_usage.py -- Demonstrates GenerativeEngineOptimizerClient
"""
from client import GenerativeEngineOptimizerClient

def main():
    client = GenerativeEngineOptimizerClient()
    result = client.optimize_text(
        product_name="GlowFlow Vitamin C Serum",
        current_description="A face serum that brightens skin and fades dark spots.",
        target_questions=["Which Vitamin C serum is best for sensitive skin?", "How long to see dark spot fading?"]
    )
    print("[GEO/AEO Optimization Result]")
    print(result['optimized_copy'])
    print(f"Hints: {result['citation_hints']}")

if __name__ == "__main__":
    main()
