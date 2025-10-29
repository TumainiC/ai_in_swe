## 1. Short Answer Questions

###  Q1: Explain how AI-driven code generation tools (e.g., GitHub Copilot) reduce development time. What are their limitations?

**Answer**
AI driven tools offer many benefits including:
1. **Speed of execution:** AI can write code in seconds to minutes which would otherwise take a developer hours  to write the same amount of code. This reduces the amount of time taken by a developer when working on a spoduct and spead up development time. 
2. **Reduced errors:** Humans are more likely to make spelling mistakes(name errors), miss a comma, a bracket (syntaxt errors) or wrongly decalre a variable type(type errors). AI is no saint but it does make singnificantly less of these errors hence giving us less buggy code. 

Some limitations of these tools also include:
- **Hallucinations:** AI often hallucinates and needs to be prompted correctly to prevent these hallucination as well as using hallucination guardrails. 
- **Over-reliance:** Due to the ease of use of AI, developers can be come over reliant and end up losing their skills in coding because of lack of practice. 
- **Cost:** AI tools are hardly free and the cost of use of these tools needs to be weighed against the benefits of the tools. 
- **Rate Limits and Context windows:** AI has rate limits on APIs and fairly small context windows that would make it difficult to be used in a large codebase. 

### Q2: Compare supervised and unsupervised learning in the context of automated bug detection.

**Answer**
*Context:* Automated bug detection involves running tests on code to determine the type of bugs found and resolve them when detected. 

In **supervised learning** we need to have laballed examples of errors in code and what those solutions for to the errors are. The limitation of this is there is a lot of effort require to collect and label this data and it is not typically readily available. 

However, in  **unsupervised learning**, we provide the model with the data without labels and let the model identify patterns in the data. This allows the model to classifiy the bugs and identify unique patterns that are not visible to the naked eye. 

### Q3: Why is bias mitigation critical when using AI for user experience personalization?

**Answer**
*Context:* **Bias mitigation** is the systematic process of identifying, measuring, and reducing unfair prejudice in algorithms, artificial intelligence (AI) systems, and human-driven decision-making. This is crucial for developing ethical, fair, and reliable AI that does not perpetuate or amplify existing societal inequities. 

Bias mitigation is critical in user experience personalization because users are incredibly diverse and this differences have traits that can be traits for discrimination against the user. Take for example an AI tool for candidate suitability detection for a job using model trained on bias data e.g predominantly caucassian candidates. This tools will wrongfully discriminate on job applicats who have different skin tones because it was trained on a non-diverse dataset. To reduce bias in this case we need to introduce diversity in the dataset and surpress model weights that bring out bias.

## 2. Case Study Analysis

### Q: How does AIOps improve software deployment efficiency? Provide two examples.

**Answer**
Examples:
- AIOps improves deployment efficiency by **shortening deployement cycles**. AI automates manual tasks to make the development and deployment processes of a product faster. In *Netflix*, they use AI to automate canary deployments and monitor performance issues beforey impact users
- AIOps ensures there are **less human errors**. This helps eliminate the possibility of configuration errors and operational mistakes. In *Facebook*, uses AI-powered test automation tools to decrease the number of errors introduced during deployment–making it run faster and more smoothly in all kinds of ways.