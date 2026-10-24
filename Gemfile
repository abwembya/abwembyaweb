source "https://rubygems.org"

# Match the Jekyll version in the latest successful managed Pages build. This site uses local layouts
# and no github-pages plugins; the umbrella gem pulled in unused vulnerable
# XML, HTTP and archive libraries. Pages hosting settings are unchanged.
gem "jekyll", "3.10.0"
gem "kramdown-parser-gfm", "~> 1.1"
gem "webrick", ">= 1.9.1", "< 2"

# Security floors for dependencies used by the local build.
gem "addressable", ">= 2.9.0", "< 3"
gem "concurrent-ruby", ">= 1.3.7", "< 2"
gem "rexml", ">= 3.4.2", "< 4"

group :development do
  gem "bundler-audit", "~> 0.9"
end
