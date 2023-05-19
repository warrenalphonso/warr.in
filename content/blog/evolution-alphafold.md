Title: Hints from AlphaFold
Date: 2023-05-08

It's surprising to me that protein folding fell to AlphaFold -- a transformer-based
architecture. There's no _very deep_ thinking going on here, like there seems to
be in eg AlphaZero. I wouldn't have guessed that protein folding would fall this
early. I would've thought that:

-   how do we even know that protein folding from heuristics (instead of just simulating
    the physics to decent precision) is possible?
-   even if it might fall to heuristics, wouldn't the heuristics probably need
    deeper thinking than humans are capable of
-   how do we know that some other paradigm of thinking of the problem isn't required?

But in ["Discussion with Yudkowsky on AGI interventions"](https://www.lesswrong.com/posts/CpvyhFy9WvCNsifkY/discussion-with-eliezer-yudkowsky-on-agi-interventions),
Yud says that he predicted intelligence would be enough to solve folding (predict
that first bullet point above is wrong) because he abstracted correctly from hints
like:

-   even human brains could contribute suggestions for searches for good protein
    configurations
-   if evolution made proteins evolvable, then there's a lot of regularity in the
    folding space which is probably exploitable

Evolution is dumb; if it figured out some space of proteins that it could easily
traverse, very shallow thinking might also be able to traverse that. Another key
point I missed is that figuring out [how natural proteins fold must be much easier
than figuring out _any_ protein will fold](https://www.biorxiv.org/content/10.1101/2021.09.19.460937v1).

It does also seem like deeper thinking than exists in AlphaFold is already do-able.
AlphaZero seems to be doing the type of deeper thinking that's really relevant for
science. Anything that plays a game has to think about what is possible given a
certain move; that seems pretty relevant when trying to do experiments to figure
out some property of nature. But it doesn't seem as useful for something like
AlphaFold.

If a key advantage in protein folding was taking advantage of [evolution being
a blind idiot god](https://www.lesswrong.com/tag/evolution-as-alien-god), then
maybe there are similar bio breakthroughs to be made with relatively shallow
thinking.
