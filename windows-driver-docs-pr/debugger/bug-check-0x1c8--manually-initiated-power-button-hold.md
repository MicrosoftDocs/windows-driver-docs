---
title: Bug Check 0x1C8 MANUALLY_INITIATED_POWER_BUTTON_HOLD
description: The MANUALLY_INITIATED_POWER_BUTTON_HOLD bug check has a value of 0x000001CE. The system was configured to initiate a bugcheck when the user holds the power button.  
keywords: ["Bug Check 0x1C8 MANUALLY_INITIATED_POWER_BUTTON_HOLD", "MANUALLY_INITIATED_POWER_BUTTON_HOLD"]
ms.author: domars
ms.date: 09/24/2018
topic_type:
- apiref
api_name:
- MANUALLY_INITIATED_POWER_BUTTON_HOLD
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1C8: MANUALLY\_INITIATED\_POWER\_BUTTON\_HOLD

The MANUALLY\_INITIATED\_POWER\_BUTTON\_HOLD has a value of  0x000001C8.

The system was configured to initiate a bugcheck when the user holds the power button for a specified length of time.  This is a diagnostic bugcheck used to capture a dump when the system is about to be hard reset with a long power button hold.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

Note that when this bug check occurs instead of the standard "blue screen" being displayed, a black background with the following text is displayed along with a % completion indicator:

“Please release the power button. We just need a few more seconds to shut down.” 


## MANUALLY\_INITIATED\_POWER\_BUTTON\_HOLD Parameters

The following parameters are displayed on the blue screen.

Parameter | Description 
|---------|--------------|
1 | Time in milliseconds the power button was held down.
2 | Pointer to nt!_POP_POWER_BUTTON_TRIAGE_BLOCK.
3 | Reserved.
4 | Reserved.


 

 




