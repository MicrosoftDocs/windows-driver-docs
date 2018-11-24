---
title: Passing and Failing a Verification
description: Passing and Failing a Verification
ms.assetid: 2639358b-eb6a-49b7-b23a-877a452917dc
keywords:
- Static Driver Verifier WDK , verification results
- StaticDV WDK , verification results
- SDV WDK , verification results
- results WDK Static Driver Verifier
- passed verification WDK Static Driver Verifier
- failed verification WDK Static Driver Verifier
- inconclusive verification WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





