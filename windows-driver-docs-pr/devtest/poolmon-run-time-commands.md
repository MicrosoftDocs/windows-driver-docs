---
title: PoolMon Run-time Commands
description: To change the display while PoolMon is running, use the run-time commands.
ms.assetid: 834f406d-5e5d-416e-90df-b52b61d70ea7
keywords:
- PoolMon Run-time Commands Driver Development Tools
topic_type:
- apiref
api_name:
- PoolMon Run-time Commands
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PoolMon Run-time Commands


To change the display while PoolMon is running, use the run-time commands. Each run-time command consists of a single keyboard character. Press the key to execute the command.

```
    [p] [( | )] [s] [TSSessionID] [i] [l] [e] [t] [a] [f] [d] [b] [m] [h | ?] [q | ESC]
```

## <span id="ddk_poolmon_run_time_commands_tools"></span><span id="DDK_POOLMON_RUN_TIME_COMMANDS_TOOLS"></span>Parameters


<span id="_______p______"></span><span id="_______P______"></span> **p**   
Toggles the display through nonpaged allocations, paged allocations, and both.

<span id="_________or__"></span><span id="_________OR__"></span> **(** or **)**  
Toggles the display between sorting by value (allocations, free operations, and bytes) and sorting by change in value. You can use either parenthesis character. They have the same effect.

<span id="_______s______"></span><span id="_______S______"></span> **s**   
Toggles the display between the system pools and the Terminal Services session pools.

<span id="_______TSSessionID______"></span><span id="_______tssessionid______"></span><span id="_______TSSESSIONID______"></span> *TSSessionID*   
Displays allocations from the specified Terminal Services session pool. *TSSessionID* represents the session ID of a Terminal Services session. It must be an integer from 0 through 9. To display all session pools or to enter session IDs greater than 9, use the **i** command.

<span id="_______i______"></span><span id="_______I______"></span> **i**   
Prompts you for the session ID of a Terminal Server session. You can respond in the following two ways:

-   To display allocations from all Terminal Services session pools, press ENTER.

-   To display allocations from a particular Terminal Services session pool, type a session ID and then press ENTER.

<span id="_______l______"></span><span id="_______L______"></span> **l**   
Toggles highlighting of changed lines on and off.

<span id="_______e______"></span><span id="_______E______"></span> **e**   
Toggles pool totals on and off. Totals appear at the bottom of the display.

<span id="_______t______"></span><span id="_______T______"></span> **t**   
Sorts by tag name.

<span id="_______a______"></span><span id="_______A______"></span> **a**   
Sorts by number of allocations. When used with a parenthesis character, the **a** key sorts by the change in allocations.

<span id="_______f______"></span><span id="_______F______"></span> **f**   
Sorts by number of free operations. When used with a parenthesis character, the **f** key sorts by the change in free operations.

<span id="_______d______"></span><span id="_______D______"></span> **d**   
Sorts by the difference between bytes allocated and bytes freed.

<span id="_______b______"></span><span id="_______B______"></span> **b**   
Sorts by bytes used. When used with a parenthesis character, the **b** key sorts by the change in bytes used.

<span id="_______m______"></span><span id="_______M______"></span> **m**   
Sorts by bytes-per-allocation. When used with a parenthesis character, the **m** key sorts by the change in bytes-per-allocations.

<span id="_________or_h"></span><span id="_________OR_H"></span> **?** or **h**  
Displays the startup command parameters, the run-time commands, and a description of the PoolMon display. To close the help display, press the ESC key.

<span id="_______q_or_ESC"></span><span id="_______q_or_esc"></span><span id="_______Q_OR_ESC"></span> **q** or **ESC**  
Stops PoolMon.









