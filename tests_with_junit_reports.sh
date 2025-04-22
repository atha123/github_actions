set -x
location=$1
#current_date=$(date '+%Y-%m-%d')

echo "Executing backend tests and also generating JUnit reports"
python3 -m pytest ${location}  --html=results/lhp.html  --self-contained-html \
--junitxml=results/lhp.xml
#python3 -m pytest ${location}  --html=results/${current_date}.html  --self-contained-html \
echo "Look for 2 reports- xml and html"

#python3 -m pytest ${location}  --html=results/${current_date}.html  --self-contained-html

