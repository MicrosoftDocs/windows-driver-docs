---
title: Special Actions for Filter Rules
description: Special Actions for Filter Rules
ms.assetid: f2631f39-02bb-4bbc-b63b-6a0200d47bc8
keywords:
- filtering trace messages, special actions WDK
- trace message filters WDK , special actions
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





