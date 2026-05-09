from google import genai
import streamlit as st

st.title("AI Business Validator")

prime = genai.Client(api_key = "AIzaSyAW4kVv2JydveDoxcNb9RQ6D8lkgn3dvIE")

audience = st.text_input("Who are your audience")
age_group = st.text_input("which is your age group")
country = st.text_input("which country you are targeting")
idea = st.text_input("Give your business idea")

prompt = f"""
You are an expert startup analyst, market researcher, and business strategist.

Generate a highly detailed Business Idea Validation Report for the following startup idea.

USER INPUTS:
- Target Audience: {audience}
- Age Group: {age_group}
- Target Country: {country}
- Business Idea: {idea}

The report should be professional, data-driven, realistic, and actionable.

Structure the response in the following format:

# Business Idea Validation Report

## 1. Executive Summary
- Explain the idea in simple terms
- What problem it solves
- Why this idea matters

## 2. Problem Analysis
- What pain points exist
- Why current solutions are insufficient
- Urgency of the problem
- Emotional and practical impact on users

## 3. Target Audience Analysis
- Describe the audience deeply
- Their behavior, interests, goals, frustrations
- Buying capability
- Online platforms they use
- How they discover products/services

## 4. Market Opportunity
- Market size estimation
- Industry growth trends
- Demand level in the target country
- Future opportunities
- TAM, SAM, and SOM estimates if possible

## 5. Competitor Analysis
Provide a table with:
- Competitor Name
- What they offer
- Strengths
- Weaknesses
- Pricing model
- Opportunity gaps

Mention both direct and indirect competitors.

## 6. Unique Value Proposition (UVP)
- What makes this idea different
- Competitive advantages
- Innovation level
- Why users would choose this product

## 7. Revenue Model Suggestions
Suggest multiple monetization methods such as:
- Subscription
- Freemium
- One-time payment
- Marketplace
- Ads
- Affiliate
- Enterprise licensing
Explain which is best and why.

## 8. Marketing Strategy
Provide:
- Organic marketing ideas
- Social media strategy
- Influencer strategy
- SEO opportunities
- Paid advertising suggestions
- Community building methods
- Viral growth ideas

## 9. MVP (Minimum Viable Product) Plan
Explain:
- Core features needed initially
- Features to avoid in version 1
- Suggested tech stack
- Estimated development difficulty
- Timeline for MVP launch

## 10. AI & Automation Opportunities
Explain how AI can improve:
- Operations
- Customer support
- Personalization
- Content generation
- Analytics
- Automation

## 11. SWOT Analysis
Provide:
- Strengths
- Weaknesses
- Opportunities
- Threats

## 12. Risk Analysis
Mention:
- Business risks
- Legal risks
- Market risks
- Competition risks
- Scaling challenges

## 13. Validation Score
Give scores out of 10 for:
- Market Demand
- Scalability
- Revenue Potential
- Competition Difficulty
- Innovation
- Execution Difficulty
- Long-term Sustainability

Also provide:
- Overall Success Probability (%)
- Risk Level (Low/Medium/High)

## 14. Step-by-Step Launch Roadmap
Provide a realistic roadmap:
- Week 1
- Month 1
- Month 3
- Month 6
- Year 1

## 15. Final Verdict
Clearly explain:
- Is this idea worth pursuing?
- Why or why not?
- Best strategy moving forward
- Recommended niche improvements
- Final motivational conclusion

IMPORTANT INSTRUCTIONS:
- Be brutally honest but constructive.
- Avoid generic advice.
- Use realistic startup thinking.
- Mention country-specific insights.
- Include examples wherever possible.
- Make the report detailed and insightful.
- Use markdown formatting.
- Use tables where appropriate.
- Assume the user wants a startup-investor-quality analysis.
"""

if st.button("GENERATE REPORT"):
    with st.spinner("Generating report..."):
        response = prime.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
            )
        st.write(response.text)








