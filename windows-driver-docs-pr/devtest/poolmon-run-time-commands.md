---
title: PoolMon Run-time Commands
description: To change the display while PoolMon is running, use the run-time commands. Each run-time command consists of a single keyboard character. Press the key to execute the command.
ms.assetid: 834f406d-5e5d-416e-90df-b52b61d70ea7
keywords: ["PoolMon Run-time Commands Driver Development Tools"]
topic_type:
- apiref
api_name:
- PoolMon Run-time Commands
api_type:
- NA
---

# PoolMon Run-time Commands


To change the display while PoolMon is running, use the run-time commands. Each run-time command consists of a single keyboard character. Press the key to execute the command.

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PoolMon%20Run-time%20Commands%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




