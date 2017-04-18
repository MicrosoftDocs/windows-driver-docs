---
title: Passing and Failing a Verification
description: Passing and Failing a Verification
ms.assetid: 2639358b-eb6a-49b7-b23a-877a452917dc
keywords: ["Static Driver Verifier WDK , verification results", "StaticDV WDK , verification results", "SDV WDK , verification results", "results WDK Static Driver Verifier", "passed verification WDK Static Driver Verifier", "failed verification WDK Static Driver Verifier", "inconclusive verification WDK Static Driver Verifier"]
---

# Passing and Failing a Verification


The SDV verification of a rule has three basic results:

-   The driver *passes* the verification.

-   The driver *fails* the verification.

-   The result is *inconclusive*.

Before drawing any conclusions based on these results, you should understand each result and be aware of the many qualifications that they entail. You should not judge any result to be a final or complete evaluation of the driver.

### <span id="verification_results"></span><span id="VERIFICATION_RESULTS"></span>Verification Results

A driver *passes* a SDV verification when, after exploring all relevant execution paths in the driver's code, the SDV [verification engine](verification-engine.md) cannot prove that the driver violated a rule that was selected for verification.

A driver *fails* a verification when the SDV verification engine proves that the driver violated a rule at least once. The violation is known as a *defect*. If the driver violated a rule more than once, SDV reports *multiple defects*.

A verification is *inconclusive* if it terminates before it completes because of timeouts (a **Timeout** result) or a memory shortage (a **Spaceout** result), or when SDV could not reach a passing or failing conclusion (an **Uncertain** result). Also, SDV might have encountered internal tool errors that prevent it from completing its tasks. (For more information about the results, see [Interpreting Static Driver Verifier Results](interpreting-static-driver-verifier-results.md).)

When a rule does not apply to the driver, for example, if the driver does not make use of the device driver interfaces that the rule verifies, SDV reports that the rule is **Not Applicable**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Passing%20and%20Failing%20a%20Verification%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




