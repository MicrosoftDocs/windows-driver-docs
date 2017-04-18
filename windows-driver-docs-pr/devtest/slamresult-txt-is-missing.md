---
title: Slamresult.txt is missing
description: Slamresult.txt is missing
ms.assetid: 41f168a1-c213-46ed-b83f-8f7eff92b4f5
---

# Slamresult.txt is missing


SDV reports this error when it cannot find slamresult.txt, an internal file that the verification engine creates and uses while verifying the driver.

Because SDV creates and uses this file in the same verification processing step (the Check step), it is rarely missing.

To resolve this error, review the time and memory limit values in the Static Driver Verifier (click the **Configuration** tab, or review the Options File and revise if necessary. Next, switch to the **Main** tab and click **Clean** to remove the files for the failed verification, and then rerun the verification.

For more information about the Check step, see [Verification Process](verification-process.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Slamresult.txt%20is%20missing%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




