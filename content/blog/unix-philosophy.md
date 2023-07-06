Title: Unix Philosophy and Effectiveness
Date: 2023-07-05

Some thoughts on [`suc`](https://the-dam.org/docs/explanations/suc.html).

The most important features of Slack for me were editing messages and threads —
can you think of a nice way to implement those here?
I guess if each message had some ID (eg timestamp), you could have some shorthand
that mentions that to reply to it or edit it. Then the `usuc` program needs to
render those. But feels like now we’re inventing protocols we have to stick to,
so it’s not very nice. But this post isn’t just a neat trick. I think the last
part about how something very simple and transparent will also be very programmable
is insightful. Eg the part about setting up notifications and having way more
control over what you want to be notified than Slack would give you

I heard on a podcast once about some software engineer who wrote the core backbone
of Facebook Marketplace in a weekend. And then he wrote the core backbone of (I
think) Facebook Ads in another weekend. Just as fun weekend projects. At the time,
I thought: a) why would someone even want to do that on their weekend, and b)
how is it even possible for someone to write that much good code in a weekend?!

But I bet those two projects looked something like this, where they just had a
cool idea about how glueing together a few small components would solve the
problem in a neat way. Then it becomes really fun to build it because it's a
very beautifully simple idea, and it becomes really possible to do it because
you're not writing that much code.
