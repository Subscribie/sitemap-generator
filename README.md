# Generate Sitemap for Subscribie onboarding pages

Print all Subscribie page urls to standard out
- subscribie pages endpoint
- ghost blog pages (api key needed- find by logging into teh ghost blog, Integrations -> api)  # noqa
- wordpress pages endpoint
- wordpress posts endpoint

# Install
```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

# Usage:
`. venv/bin/activate && python3 app.py <ghost-api-key>`

# Automate

Install as cron and pipe output to sitemap.txt

## Example cron

`run.sh`
```
#!/bin/bash
cd /<location-of>/sitemap-generator
. venv/bin/activate
python app.py <ghost-api-key> /<destination>/sitemap.txt

# Ping google to let them know things might have been added
# See https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap#addsitemap
curl https://www.google.com/ping?sitemap=https://subscriptionwebsitebuilder.co.uk/sitemap.txt
```

## Example output

```
https://subscriptionwebsitebuilder.co.uk/p/automated-payment-system-in-uk/
https://subscriptionwebsitebuilder.co.uk/p/how-to-let-subscribers-login-to-view-their-subscriptions/
https://subscriptionwebsitebuilder.co.uk/p/start-a-subscription-website/
https://subscriptionwebsitebuilder.co.uk/page/pricing
https://subscriptionwebsitebuilder.co.uk/page/subscription_website_builder_uk
https://subscriptionwebsitebuilder.co.uk/page/faq
https://subscriptionwebsitebuilder.co.uk/page/About
http://subscriptionwebsitebuilder.co.uk/blog/subscription-boxes-have-grew-800-since-2014/
http://subscriptionwebsitebuilder.co.uk/blog/why-are-more-businesses-turning-to-subscription-models/
http://subscriptionwebsitebuilder.co.uk/blog/seo-strategy-advice-for-subscription-website-builder/
http://subscriptionwebsitebuilder.co.uk/blog/stripe-made-simple/
http://subscriptionwebsitebuilder.co.uk/blog/outline-of-gocardless/
http://subscriptionwebsitebuilder.co.uk/blog/challenges-in-the-recurring/
http://subscriptionwebsitebuilder.co.uk/blog/should-i-use-a-website-builder/
http://subscriptionwebsitebuilder.co.uk/blog/how-to-build-a-subscription-website/
http://subscriptionwebsitebuilder.co.uk/blog/advice-on-setting-up-a-subscription-website/
http://subscriptionwebsitebuilder.co.uk/blog/helpful-tips-for-subscription-website-builder/
http://subscriptionwebsitebuilder.co.uk/blog/how-to-set-up-stripe/
```
