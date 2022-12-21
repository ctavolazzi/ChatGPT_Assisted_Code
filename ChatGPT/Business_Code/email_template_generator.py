template = "Hello, I'm excited to introduce you to {company_name}, the ultimate destination for {target_market} who love {product_or_service}. We offer a unique selection of {products_or_services}, including {examples}, that are designed to appeal to {target_market_adjective}.\nOur target market is growing rapidly, as more and more {target_market} are {activity} and looking for ways to express their passion for {passion}. We have identified a gap in the market for {unique_product_or_service}, and we are well-positioned to capitalize on this opportunity.\nWe have already incurred startup costs of approximately {startup_costs}, and we project sales of {projected_sales} in the first year. Our financial plan shows a profit of {projected_profit} in the first year, and we have plans to expand and increase sales in the future.\nWe are seeking funding from investors to support the initial growth of our business. We believe that our unique product offering and experienced management team make {company_name} an attractive investment opportunity.\nThank you for considering investing in {company_name}. We look forward to discussing this opportunity further with you and answering any questions you may have."

company_name = "Gentle Bull"
target_market = "software developers"
product_or_service = "music festivals"
products_or_services = "merchandise"
examples = "t-shirts, hats, and accessories"
target_market_adjective = "tech-savvy festival-goers"
activity = "attending music festivals"
passion = "both technology and music"
unique_product_or_service = "high-quality, tech-themed festival merchandise"
startup_costs = "$10,000"
projected_sales = "$25,000"
projected_profit = "$5,000"

message = template.format(company_name=company_name, target_market=target_market, product_or_service=product_or_service, products_or_services=products_or_services, examples=examples, target_market_adjective=target_market_adjective, activity=activity, passion=passion, unique_product_or_service=unique_product_or_service, startup_costs=startup_costs, projected_sales=projected_sales, projected_profit=projected_profit)
