---
title: WHQL Release Signature
description: Learn how to obtain a WHQL release signature for your driver package by testing it with the Windows Hardware Lab Kit (HLK).
ms.date: 07/11/2025
keywords:
- driver signing WDK , WHQL digital signatures
- signing drivers WDK , WHQL digital signatures
- digital signatures WDK , WHQL
- signatures WDK , WHQL
- WHQL digital signatures WDK
- public release driver signing WDK , WHQL
- release signing WDK , WHQL
ms.topic: how-to
---

# WHQL release signature

Your Windows Hardware Quality Labs (WHQL) digitally signed driver package can be distributed through the Windows Update program. WHQL can digitally sign your [driver packages](driver-packages.md) if they pass [Windows Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) testing.

The process of obtaining a WHQL release signature is part of the HLK. A WHQL release signature consists of a digitally signed [catalog file](catalog-files.md). The digital signature doesn't change the driver binary files or the INF (_.inf_) file that you submit for testing.

To obtain a WHQL release signature, complete the following actions:

- Test the [driver package](driver-packages.md) with the Windows Hardware Certification Kit (HCK) and verify that the driver package is compatible with Microsoft Windows. After you install the HCK, the Driver Test Manager (DTM) is run to test and verify the driver package. For more information, see the [HLK documentation](/windows-hardware/test/hlk/).

- Submit DTM test logs to the Windows Quality Online Services to obtain a WHQL release signature for the driver package. For more information, see the [HLK documentation](/windows-hardware/test/hlk/).

You can embed a signature in a driver file by using WHQL. For more information, see the [Windows Hardware Quality Labs](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) website.