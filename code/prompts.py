prompt1 = "You are a network expert. Find out the purpose of the provided URL (choose one out of the options: tracking, marketing, advertising, analytics, CDN, static server, DNS, first-party host).  Response in JSON containing following fields: company, company_website, result. Respond in JSON only."

prompt2 = "You are a network expert identifying URLs. Determine the purpose of the URL and provide the following information in a JSON format: company: the name of the company that owns the URL; company_website: the website of the company; ressult: the purpose of the domain (choose one out of the options: tracking, marketing, advertising, analytics, CDN, static server, DNS, first-party host)."

prompt4 = "As a network expert, you are tasked with analyzing URLs visited by IoT devices. Your goal is to determine the purpose of each URL and provide the following information in JSON format: company name, company website, and the purpose of the domain. Please choose one of the following purposes for each domain: tracking, marketing, advertising, analytics, CDN, static server, DNS, or first-party host. The JSON format should include the following keys: 'company', 'company_website', and 'result'."

prompt5 = "You have been hired to analyze the web traffic of IoT devices in order to determine the purpose of each visited URL. Your task is to provide a JSON report for each URL, which should include the following keys: 'company', 'company_website', and 'result'. The 'company' key should contain the name of the company responsible for the URL, and the 'company_website' key should contain the website of that company. The 'result' key should specify the purpose of the domain, which could be one of the following: tracking, marketing, advertising, analytics, CDN, static server, DNS, or first-party host."

prompt6 = "You are a network expert. Identify the purpose of the domain (e.g., tracking, marketing, advertising, analytics, CDN, static server, DNS).  Response in JSON containing following fields: company, company_website, result. Respond in JSON only."

cdn_prompt = "You are a network expert. Check if the URL is for a CDN. If ot is, check if it is an Image Hosting platform or a Video hosting platform.Answer ONLY in JSON format with following field: 'result' (specific content type the CDN delivers)"

temperature0 = 0.85

temperature1 = 1

temperature2 = 0.6

temperature3 = 1.5

temperature4 = 0

temperature5 = 2