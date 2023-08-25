Title: Clinical Trial Costs Per Patient
Date: 2023-08-15
Modified: 2023-08-24

After the hard work of creating a candidate drug -- [the initial insights to try out
a particular compound in some chemical search space, the enormous high-throughput
screening of small variations on a lead molecule, extensive animal testing](https://www.goodreads.com/book/show/3484805-breakthrough) --
the promising drug needs to actually be tested in humans. We call these tests
clincial trials. There are typically four different types of clinical tirals:

- Phase I: testing the drug in healthy humans to check for toxic side effects and
  maximum dosage
- Phase II: testing the drug in a few people with the disease group the drug is
  meant to test to check for efficacy
- Phase III: scaling up to many people in the disease group, check for side effects
- Phase IV: studies after initial approval, typically on a patient group already
  tested in a previous phase and run for a longer time period

Running trials is hard work; you've got to screen for patients, track patient progress,
measure many things, keep results organized for months or years.

A [2014 study by Berndt and Cockburn](https://www.bls.gov/opub/mlr/2014/article/price-indexes-for-clinical-trial-research-a-feasibility-study.htm)
found that costs for trials were *increasing really quickly*. (This study, and a
lot of others I've found, is based on Medidata's PICAS database -- I wonder if I
can get access to that?)

(There are other trends that contribute: namely number of patients and the geographic
distribution is changing with Phase I/II recruiting less and Phase III/IV recruiting
more, but that shouldn't show up much when discussing cost per patient.)

## Really quickly compared to what?

The NIH publishes the [Biomedical Research and Development Price Index (BRDPI)](https://officeofbudget.od.nih.gov/gbipriceindexes.html),
which indicates how much the NIH budget must change to maintain purchasing power.
That's a good starting point for checking whether increases in clincial trial
pricing are surprising:

![Average Trial Cost and BRDPI]({static}/images/trial-cost-and-brdpi.png)

## How much of this is because of increased site work?

If price is increasing, it might be because trials are contributing more value than
they were in the past, eg checking more endpoints, doing more complex procedures.
Berndt14 uses a measure of "Site Work Effort" to approximate this:

![Average Site Work Effort]({static}/images/site-work-effort.png)

That seems to follow the rise in prices reasonably well. When we divide the mean
price by mean site work effort, we follow the R&D price index more closely:

![Mean Cost Normalized by Mean SWE]({static}/images/work-normalized-cost.png)

(Well, take this with a grain of salt because $avg(\frac{a}{b}) \neq \frac{avg(a)}{avg(b)}$.)

### What is site work, concretely?

Work is measured in [relative value units (RVU)](https://en.wikipedia.org/wiki/Relative_value_unit),
which are a
Medicare measure of value added by a physician service. If some services provided
during clinical trials don't have a Medicare RVU, [the authors rely on a panel of
physicians at Tufts to estimate the time spent per procedure](https://pubmed.ncbi.nlm.nih.gov/18806521/).

Here are some common types of procedures with their occurences per trial protocol
from [Getz08](https://pubmed.ncbi.nlm.nih.gov/18806521/):

![Procedure Types]({static}/images/procedure-types.png)

It'd be useful to check how this varies with therapeutic class. Getting into the
details of which procedures are common for different therapeutic areas and which
sorts of procedures require the least amount of effort or are the most scalable
seems important. I shied away from doing this analysis because having just two
data points (1999, 2005) really means the analysis isn't very helpful. I'll look
for more recent studies before continuing the analysis.

## Can we tease out any trends about economies of scale?

Berndt14 does some regression analyses to look for relationships between
cost-per-patient and total number of patients in a trial or total site work effort.

Here I've plotted the regression coefficients for how cost-per-patient (TGPP: total
grant cost per patient) depends on total number of patients. This is a log-log
regression: $\ln(\text{TGPP}) = b + a \ln(\text{NPATIENTS})$, where $a$ is the
regression coefficient being graphed. Notice that for "economies of scale", we'd
want the regression coefficient to be *negative*: average cost decreases as number
of patients increases.

(Aside: we're doing a log-log analysis to focus more on
[elasticity](https://en.wikipedia.org/wiki/Elasticity_of_a_function). If we used
just $\text{NPATIENTS}$ and $\text{TGPP}$, the analysis would tell us that a
one-unit increase in former causes an $a$-unit increase in latter. If we use the
logarithms of both, the analysis instead tells us that a 1 *percent* increase in
former causes an $a$ *percent* increase in the latter.)

![Economies of Scale]({static}/images/trial-economies-of-scale.png)

This is alarming! Trials in the US have slight economies of scale, but trials in
the rest of the world have *huge* diseconomies of scale in Phase III and IV. Economies
of scale are really only relevant in Phase III and IV trials because they have hundreds
or thousands of patients, while earlier phases have tens of patients.

Here's another regression analysis for how log cost-per-patient varies with site
work effort. We expepct
this to be positive: more work probably means each patient is more expensive. (Here
we're looking at a semi-log analysis: a one-unit increase in SWE causes an $a$ percent
increase in TGPP.)

![SWE Cost]({static}/images/swe-cost.png)

## Why does the rest of the world have large diseconomies of scale?

I'm still working on this, and I'll spin it out into a separate post! Do email me
if you have any ideas for how to investigate this.
