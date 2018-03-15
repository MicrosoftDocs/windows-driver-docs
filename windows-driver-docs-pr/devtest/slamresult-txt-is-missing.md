---
title: Slamresult.txt is missing
description: Slamresult.txt is missing
ms.assetid: 41f168a1-c213-46ed-b83f-8f7eff92b4f5
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Slamresult.txt is missing


SDV reports this error when it cannot find slamresult.txt, an internal file that the verification engine creates and uses while verifying the driver.

Because SDV creates and uses this file in the same verification processing step (the Check step), it is rarely missing.

To resolve this error, review the time and memory limit values in the Static Driver Verifier (click the **Configuration** tab, or review the Options File and revise if necessary. Next, switch to the **Main** tab and click **Clean** to remove the files for the failed verification, and then rerun the verification.

For more information about the Check step, see [Verification Process](verification-process.md).

 

 





