Title: Unix Philosophy and Effectiveness
Date: 2023-07-05
Modified: 2023-07-06

Some thoughts on [`suc`](https://the-dam.org/docs/explanations/suc.html).

---

The most important features of Slack for me were editing messages and threads —-
can you think of a nice way to implement those here?

We could fold it into the format by introducing some protocol that referenced a
previous message's timestamp to reply or edit it.
Then we've got to modify `usuc` to render threads and edits properly. This introduces
a lot of complexity because when rendering a thread/message, we've got to search the text
file to find all replies/edits.

Alternatively, we could go for
an [easily-deleteable implementation](https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to):
add new "replies" and "edits" databases that
link message timestamps together to form a chain. We've got the same problem with
adding complexity to `usuc`, but now we've got to worry about order/delay of writes
to the databases.

[Text stream interfaces are important to the Unix philosophy](http://www.catb.org/esr/writings/taoup/html/ch05s01.html).
These features both mess with the ordered nature of the text stream; I
think that's why I'm having trouble integrating them.

---

This post isn’t just a neat trick. I think the last
part about how something very simple and transparent will also be very programmable
is insightful, eg the part about setting up notifications and having way more
control over what you want to be notified than Slack would give you.

---

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
