---
title: Call to action and resources (threat modeling for drivers)
description: This article contains call to action recommendations and resources for threat modeling for drivers.
ms.assetid: F0DC2461-6C9A-451A-8485-407299DBEC0E
ms.author: windowsdriverdev
ms.date: 06/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Call to action and resources (threat modeling for drivers)


**Last updated:**

-   January 27, 2017

This article contains call to action recommendations and resources for threat modeling for drivers.

## <span id="Call_to_action"></span><span id="call_to_action"></span><span id="CALL_TO_ACTION"></span>Call to action


For driver developers:

-   Consider making threat modeling part of driver design.
-   Take steps to efficiently [Mitigate threats](#mitigate)
-   Become familiar with the security and reliability issues that apply to your driver and device type. For more information, see the device-specific sections of the Windows Device Driver Kit (WDK).
-   Understand which checks the operating system, I/O manager, and any higher-level drivers perform before user requests reach your driver—and which checks they do not perform.
-   Use tools from the WDK to test and verify your driver.
-   [Review public databases of known threats and software vulnerabilities](#reviewthreats)

## <span id="Mitigate"></span><span id="mitigate"></span><span id="MITIGATE"></span>Mitigate threats


Determining how and where a driver might be attacked is not enough. You must then assess these potential threats, determine their relative priorities, and devise a mitigation strategy.

### <span id="The_DREAD_approach"></span><span id="the_dread_approach"></span><span id="THE_DREAD_APPROACH"></span>The DREAD approach

DREAD is an acronym that describes five criteria for assessing threats to software. DREAD stands for:

-   **D**amage
-   **R**eproducibility
-   **E**xploitability
-   **A**ffected users
-   **D**iscoverability

To prioritize the threats to your driver, rank each threat from 1 to 10 on all 5 of the DREAD assessment criteria, and then add the scores and divide by 5 (the number of criteria). The result is a numeric score between 1 and 10 for each threat. High scores indicate serious threats.

-   **Damage**. Assessing the damage that could result from a security attack is obviously a critical part of threat modeling. Damage can include data loss, hardware or media failure, substandard performance, or any similar measure that applies to your device and its operating environment.
-   **Reproducibility** is a measure of how often a specified type of attack will succeed. An easily reproducible threat is more likely to be exploited than a vulnerability that occurs rarely or unpredictable. For example, threats to features that are installed by default, or are used in every potential code path, are highly reproducible.
-   **Exploitability** assesses the effort and expertise that are required to mount an attack. A threat that can be attacked by a relatively inexperienced college student is highly exploitable. An attack that requires highly skilled personnel and is expensive to carry out is less exploitable.

    In assessing exploitability, consider also the number of potential attackers. A threat that can be exploited by any remote, anonymous user is more exploitable than one that requires an onsite, highly authorized user.

-   **Affected Users**. The number of users that could be affected by an attack is another important factor in assessing a threat. An attack that could affect at most one or two users would rate relatively low on this measure. Conversely, a denial-of-service attack that crashes a network server could affect thousands of users and therefore would rate much higher.
-   **Discoverability** is the likelihood that a threat will be exploited. Discoverability is difficult to estimate accurately. The safest approach is to assume that any vulnerability will eventually be taken advantage of and, consequently, to rely on the other measures to establish the relative ranking of the threat.

**Sample: Assessing Threats**

Continuing with the example discussed in [Create threat models for drivers](create-threat-models-for-drivers.md), the following table shows how a designer might assess the hypothetical denial-of-service attack:

| DREAD Criterion | Score   | Comments                                                                |
|-----------------|---------|-------------------------------------------------------------------------|
| Damage          | 8       | Disrupts work temporarily, but causes no permanent damage or data loss. |
| Reproducibility | 10      | Causes the device to fail every time.                                   |
| Exploitability  | 7       | Requires a focused effort to determine the command sequence.            |
| Affected users  | 10      | Affects every model of this device on the market.                       |
| Discoverability | 10      | Assumes that every potential threat will be discovered.                 |
| **Total:**      | **9.0** | **Mitigating this problem is high priority.**                           |

 

If possible, your driver design should mitigate against all the threats that your model exposes. However, in some cases, mitigation might not be practical. For example, consider an attack that potentially affects very few users and is unlikely to result in loss of data or system usability. If mitigating such a threat requires several months of additional effort, you might reasonably choose to spend additional time testing the driver instead. Nevertheless, remember that eventually a malicious user is likely to find the vulnerability and mount an attack, and then the driver will require a patch for the problem.

## <span id="Resources"></span><span id="resources"></span><span id="RESOURCES"></span>Resources


**Books**

*Writing Secure Code*, Second Edition by Michael Howard and David LeBlanc

*24 Deadly Sins of Software Security: Programming Flaws and How to Fix Them*, First Edition by Michael Howard, David LeBlanc and John Viega

*The art of software security assessment : identifying and preventing software vulnerabilities*, by Mark Dowd, John McDonald and Justin Schuh

**Microsoft Hardware and Driver Developer Information**

[Common Driver Reliability Problems](http://download.microsoft.com/download/5/7/7/577a5684-8a83-43ae-9272-ff260a9c20e2/drvqa.doc) white paper

[Cancel Logic in Windows Drivers](https://msdn.microsoft.com/library/windows/hardware/dn653289) white paper

[Windows security model: what every driver writer needs to know](windows-security-model--what-every-driver-writer-needs-to-know.md)

**Microsoft Windows Driver Development Kit (DDK)**

See [Driver Programming Techniques](https://msdn.microsoft.com/library/windows/hardware/ff544177) in [Kernel-Mode Driver Architecture](https://msdn.microsoft.com/library/windows/hardware/ff557560)

**Test Tools**

See [Windows Hardware Lab Kit](https://msdn.microsoft.com/library/windows/hardware/dn930814) in [Test for performance and compatibility](https://msdn.microsoft.com/windows/hardware/commercialize/test/index)

## <span id="ReviewThreats"></span><span id="reviewthreats"></span><span id="REVIEWTHREATS"></span>Review public databases of known threats and software vulnerabilities


To expand your knowledge of software threats, review the available public databases of known threats and software vulnerabilities.

-   Common Vulnerabilities and Exposures (CVE): <https://cve.mitre.org/>
-   Common Weakness Enumeration: <https://cwe.mitre.org/>
-   Common Attack Pattern Enumeration and Classification: <https://capec.mitre.org/index.html>
-   NIST maintains a site that describes how vulnerabilities are cataloged: <https://samate.nist.gov/BF/>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design\hw_design]:%20Call%20to%20action%20and%20resources%20%28threat%20modeling%20for%20drivers%29%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




