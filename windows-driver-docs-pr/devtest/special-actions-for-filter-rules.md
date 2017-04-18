---
title: Special Actions for Filter Rules
description: Special Actions for Filter Rules
ms.assetid: f2631f39-02bb-4bbc-b63b-6a0200d47bc8
keywords: ["filtering trace messages, special actions WDK", "trace message filters WDK , special actions"]
---

# Special Actions for Filter Rules


There are three special values in the **Action** element of a filter rule. The following list describes these actions.

<span id="Ignore"></span><span id="ignore"></span><span id="IGNORE"></span>**Ignore**  
Ignores the rule. This action is an alternative to deleting the rule.

<span id="Discard"></span><span id="discard"></span><span id="DISCARD"></span>**Discard**  
Hides the trace message. This action is effective only on new messages. For messages in a log file, you must save and reload the log. For instructions, see "Comments" below.

<span id="AND"></span><span id="and"></span>**AND**  
Creates a multi-line rule that is connected by the AND operation. All conditions in a multi-line rule must be satisfied for the action to be applied. By default, all rules in a filter are connected by the OR operator.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

Most filter rules are effective immediately. Filters rules that use the **Discard** action are effective only on messages that arrive after the rule is applied. To apply a **Discard** rule to an existing log file, [save the workspace](saving-or-resaving-a-workspace.md), [remove the trace session](removing-a-trace-session.md), and then [open the workspace](opening-a-workspace.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Special%20Actions%20for%20Filter%20Rules%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




