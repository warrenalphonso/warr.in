Title: Some Questions I Had About Pharma and Drug Development
Date: 2023-07-16
Modified: 2023-07-20

## Questions around R&D spending

- Can I neatly split up expected costs per trial period: preclinical, clinical? Or
  does it vary too much?
    - This is Figure 3 in *Entrepreneur's Guide to a Biotech Startup* by Kolchinsky which was written in 2001: ![Average drug development costs in time and money by clinical trial]({static}/images/Kolchinsky01-Fig3.png)
        - Have things changed since 2001? Is this even accurate?
            - [Here's a study for a $2B number, which is cited a *lot*](https://www.sciencedirect.com/science/article/abs/pii/S0167629616000291)
                - ![Phase 3 hurts]({static}/images/DiMasi16-Table2.png)
            - I need to just [look at the study](https://pubmed.ncbi.nlm.nih.gov/30264133/).
              Seems like drugs for smaller amounts of people have easier testing and
              difference in cost with larger drug trials is like 100x.
        - But why does each trial cost what it does?
- What drug types are most expensive and why?
    - [this site](https://www.srgtalent.com/blog/why-are-clinical-trials-of-new-drugs-so-expensive)
      gives costs for different types of drugs. Average cost for clinical trial for
      one patient is $36.5K (which seems crazy high!). For cancer, it's $60K. For
      infectious diseases, it's $17K.
        - The general cost breakdown is:
            - 20% on "clinical procedures"
            - 20% on "staff"
            - 14% on "site monitoring"
            - 12% on "site retention"
            - 8% on "lab costs"
- What would a very cheap drug to develop look like?
    - What class of drugs does a poorly-funded startup have a chance of developing?
- How cheaper does AlphaFold make things?
- How much does global pharma spend on R&D?
    - Where is this allocated? How much to drug design? What other parts of R&D exist?
    - Does it now make sense to get more granularity on where money is allocated? Like,
    what types of drugs get the most funding to be developed and why? What get the
    least?
- What areas have just a single big company or two looking at them? Where are
  things likely to not be very competitive?
- What do more efficient clinical trials look like?
    - ["Adaptive designs in clinical trials: why use them, and how to run and report them"](https://bmcmedicine.biomedcentral.com/articles/10.1186/s12916-018-1017-7)
    - Another thing from just thinking about this is that it seems we're repeating an
      insane amount of work for each thing? Suppose we know two drugs are pretty similar
      for how they work; does the FDA allow for fewer trials then? Can we be more
      Bayesian here? Can ML help with that?
        - Instead of just being like "we're not being Bayesian" or "eh, the FDA is letting
          us be pretty Bayesian", *just look at the evidence!* Look at the history of
          drugs in clinical trials. How close were they to other drugs at the time? It
          sure *seems* like there's just a few classes of drugs when I go to Walmart Pharmacy
          for eg pain drugs.
- Where is R&D focusing?
    - [Sarah Constantin says there are a few thousand drugs being studied at any one time, ultimately because pharma isn't competitive](https://www.lesswrong.com/posts/BhGSXuvTvEtYtJXBe/list-of-civilisational-inadequacy?commentId=ynRYxWKBARXXEApKy)
        - Is that true? How do I get better approximations on that?
        - Are most of these drugs focused on specific cause areas?
        - Thousands isn't a lot. I could keep broad-strokes tabs on those drugs. Are they
          all publicly disclosed? In the US, anything in "clinical trials" (phase I, II, or III)
          must be disclosed on clinicaltrials.gov! EU has their own website. That's
          awesome.
            - The next step is to make a list of all these drugs and what broad category
              they're in. That seems very doable. I'll start a new section below because
              ClinicalTrials.gov has a lot of maybe useful links.
    - [Here's an analysis that says we have 20K drugs in pipeline in 2021](https://pharmaintelligence.informa.com/~/media/informa-shop-window/pharma/2021/pharmaprojects_jp/pharma-rd-annual-review-2022_lr_rvsd_en_final.pdf)
        - [Infographic for above](https://images.intelligence.informa.com/Web/InformaUKLimited/%7B120ce195-3040-41d7-9b17-94c6aec9760f%7D_12647_Informa_R_D_Infographic_2022_8.pdf)
    - [here's a statistica graph, but I bet it uses the same info?](https://www.statista.com/statistics/791263/total-r-and-d-pipeline-size-timeline-worldwide/)
- Are there branches of the FDA that are easier to get past?
    - [Loyal had to get approval from some veterinary branch for example](https://blog.loyalfordogs.com/loyals-latest-milestone-the-first-longevity-clinical-study-design-supported-by-the-fda/)

## Some ideas for things I should read

- Maybe the Genentech book, but I'm not so sure. That's more historical; I don't
  care yet, right?
- The [FDA's setup](https://www.law.cornell.edu/cfr/text/21/chapter-I).
  N Horwitz says you'll be surprised what's not in it?
- SEC to see company financials?
- https://medium.com/@david.eil/does-america-have-to-overpay-for-health-care-to-drive-innovation-8b974922d8c
- https://www.cbo.gov/publication/57126
- Read *Entrepreneur's Guide to Biotech Startup*
- Read *Pharmagellan's Guide to Clinical Trials*
  - Part 2 Special Topics has a bunch of independent interesting things I could
    Anki in 30 minutes a piece.
- Read *How Drugs Work*
- Read *Which Country Has the World's Best Health Care* by Emanuel
- https://slatestarcodex.com/2016/09/07/reverse-voxsplaining-brand-name-drugs/
- https://www.science.org/content/blog-post/drugs-2015-2021
