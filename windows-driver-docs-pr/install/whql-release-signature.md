---
title: WHQL Release Signature
description: WHQL Release Signature
ms.assetid: edc815d4-596c-4f50-9bff-029b8ea19a0a
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


[Driver packages](driver-packages.md) that pass [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893) testing can be digitally-signed by WHQL. If your driver package is digitally-signed by WHQL, it can be distributed through the [Windows Update](https://msdn.microsoft.com/windows-drivers/develop/distributing_a_driver_package_win8) program or other Microsoft-supported distribution mechanisms.

Obtaining a WHQL release signature is part of the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893). A WHQL release signature consists of a digitally-signed [catalog file](catalog-files.md). The digital signature does not change the driver binary files or the INF file that you submit for testing.

Obtaining a WHQL release signature consists of the following:

-   Testing the [driver package](driver-packages.md) with the Windows HCK to verify that the driver package is compatible with Microsoft Windows. Once the HCK is installed, the Driver Test Manager (DTM) is run to test and verify the driver package. For more information, see the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893).

-   Submitting DTM test logs to the Windows Quality Online Services to obtain a WHQL release signature for the driver package. For more information, see the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893).

For more information about WHQL, see the [Windows Hardware Quality Labs](http://go.microsoft.com/fwlink/p/?linkid=8705) website.

**Note**  WHQL does not embed signatures in driver files. You can embed a signature in a driver file using a third-party commercial [release certificate](release-certificates.md). Embed the signature in the driver file before submitting the driver package to WHQL.

 

 

 





