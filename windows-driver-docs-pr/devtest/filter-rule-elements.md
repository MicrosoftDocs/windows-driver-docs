---
title: Filter Rule Elements
description: Filter Rule Elements
ms.assetid: 448da1f1-5eea-4159-ba19-cda14ebebae6
keywords:
- filtering trace messages, changeable elements WDK
- trace message filters WDK , changeable elements
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Rule Elements


The following list describes the elements of a filter rule that you can modify in the **Manage Filters** dialog box:

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**  
A user-defined text string that describes the rule. Type any phrase that helps you identify the rule.

<span id="Column"></span><span id="column"></span><span id="COLUMN"></span>**Column**  
The fields in the trace message or [trace message prefix](trace-message-prefix.md). Select one field for each line in the rule.

<span id="Operation"></span><span id="operation"></span><span id="OPERATION"></span>**Operation**  
A logical operation that relates the value of the **Column** element to the value of the **Text** element.

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>**Text**  
A text field in which you specify the condition that the value in the **Column** element must meet in order for the rule to be applied.

<span id="Action"></span><span id="action"></span><span id="ACTION"></span>**Action**  
The action that is performed on the trace message if it meets the conditions specified in the **Text** field.

 

 





