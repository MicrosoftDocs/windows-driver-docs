---
title: WHQL Release Signature
description: WHQL Release Signature
keywords:
- driver signing WDK , WHQL digital signatures
- signing drivers WDK , WHQL digital signatures
- digital signatures WDK , WHQL
- signatures WDK , WHQL
- WHQL digital signatures WDK
- public release driver signing WDK , WHQL
- release signing WDK , WHQL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WHQL Release Signature


[Driver packages](driver-packages.md) that pass [Windows Hardware Certification Kit (HCK)](/windows-hardware/test/hlk/) testing can be digitally-signed by WHQL. If your driver package is digitally-signed by WHQL, it can be distributed through the [Windows Update](/windows-hardware/drivers) program or other Microsoft-supported distribution mechanisms.

Obtaining a WHQL release signature is part of the [Windows Hardware Certification Kit (HCK)](/windows-hardware/test/hlk/). A WHQL release signature consists of a digitally-signed [catalog file](catalog-files.md). The digital signature does not change the driver binary files or the INF file that you submit for testing.

Obtaining a WHQL release signature consists of the following:

-   Testing the [driver package](driver-packages.md) with the Windows HCK to verify that the driver package is compatible with Microsoft Windows. Once the HCK is installed, the Driver Test Manager (DTM) is run to test and verify the driver package. For more information, see the [Windows Hardware Certification Kit (HCK)](/windows-hardware/test/hlk/).

-   Submitting DTM test logs to the Windows Quality Online Services to obtain a WHQL release signature for the driver package. For more information, see the [Windows Hardware Certification Kit (HCK)](/windows-hardware/test/hlk/).

For more information about WHQL, see the [Windows Hardware Quality Labs](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) website.

**Note**  WHQL does not embed signatures in driver files. You can embed a signature in a driver file using a third-party commercial [release certificate](release-certificates.md). Embed the signature in the driver file before submitting the driver package to WHQL.

 

