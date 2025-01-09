---
title: Driver security guidance
description: This section contains information on enhancing driver security.
ms.assetid: 50D09948-8CE2-446F-A208-35F7B3795A6B
ms.date: 01/08/2025
ms.topic: article
---

# Driver security guidance

This section provides crucial advice on improving the security of drivers in Windows.

## Windows is mission critical

Windows is used by hospitals, 911 systems, airports and other vital institutions and organizations. The world relies on Windows to be reliable and secure.

In these critical environments, any failure or compromise in the operating system can have severe consequences. Therefore, ensuring that drivers – the software that allows the operating system to communicate with hardware devices – are secure and reliable is paramount. The integrity of these systems is non-negotiable, and driver developers play a crucial role in maintaining this important functionality.

## Windows is an open ecosystem 

To allow unique software solutions to be created by partners, Windows is an open ecosystem that allows full and direct kernel memory access. This access is helpful for enabling advanced functionalities but comes with significant responsibilities. When writing drivers, developers must follow secure coding guidelines to prevent vulnerabilities that could be exploited by malicious actors.

## Increasing threat

Today’s threat landscape is unlike any we’ve seen before. Attacks are growing in speed, scale, and sophistication. In 2015, the Microsoft identity systems were detecting around 115 password attacks per second. Less than a decade later, that number has surged 3,378% to more than 4,000 password attacks per second. With more than 600 million attacks of all types of per day targeting Microsoft customers, creating secure driver code must be a central priority. For more information about the incredible growth in cyber attacks, see [10 essential insights from the Microsoft Digital Defense Report 2024](https://www.microsoft.com/en-us/security/security-insider/intelligence-reports/10-essential-insights-from-the-Microsoft-Digital-Defense-Report-2024).

Because of the critical importance of cyber security, the United States government has issued the [Cybersecurity Executive Order](https://www.whitehouse.gov/briefing-room/statements-releases/2021/05/12/fact-sheet-president-signs-executive-order-charting-new-course-to-improve-the-nations-cybersecurity-and-protect-federal-government-networks/). For a summary of the required actions to strengthen security and address ever evolving threats, see [The Cybersecurity Executive Order: What’s Next for Federal Agencies?](https://www.microsoft.com/industry/microsoft-in-business/security/2021/06/17/the-cybersecurity-executive-order-whats-next-for-federal-agencies/).

This ominous threat landscape requires stronger and more comprehensive security approaches than ever before, across all devices and technologies we use in our lives. For driver developers, this means implementing robust security measures to protect against these escalating threats.

## Benefits of shipping a secure and reliable driver

Shipping secure and reliable drivers offers many benefits:

|Benefit                  | Description |
|------------------------ |------------ |
| Avoidance of costly security incidents | Responding to a security incident is costly, stressful and can significantly impact the viability of a business. |
| Repeat and referral sales | Satisfied customers are more likely to make repeat purchases and refer others. With a security incident, customers are likely to re-evaluate vendors and consider moving their business to a new partner.  Customers are more likely to trust and recommend your products if they work as they should. |
| Lower support costs | Fewer security issues and crashes mean reduced support costs and less downtime. |
| Increased security = Increased product reliability | Work that is done to clean up incorrect memory access that creates security holes, increases product reliability. When Windows detects that incorrect memory access is taking place, it will shut down the OS and display a blue error screen. |

The shared goal is to reduce the significant impact that a failed driver has on our customers lives and their use of Windows in critical environments.

:::image type="content" source="images/bug-check-example-blue-screen-page-fault.png" alt-text="Screenshot of a Windows 10 blue screen displaying a bug check with a QR code.":::

## Shared responsibility in the Windows and partner ecosystem

Ensuring the security of Windows systems is a shared responsibility between Microsoft and its partners. This partnership is essential for creating a secure ecosystem that users can trust. As a partner that creates Windows drivers, at minimum, you must do the following. 

- Adhere to Security Guidelines: Follow Microsoft’s security guidelines for driver development. A great place to start is the [Driver security checklist](driver-security-checklist.md).

- Monitor driver reliability data: As part of distributing your driver using Windows Update, driver reliability measures will be available, such as the number of machines without a kernel mode crash. For more information about driver distribution and the health measures, see [Driver flighting](/windows-hardware/drivers/dashboard/driver-flighting).

- Stay Informed: Keep abreast of the latest security threats and best practices by participating in security summits and forums. Two key resources are the [Microsoft Security Blog](https://www.microsoft.com/security/blog/) and the [Microsoft Offensive Research & Security Engineering (MORSE) Security Blog](https://www.microsoft.com/security/blog/author/microsoft-offensive-research-security-engineering-team/).

- Use the resources provided by CISA: Align with the Cybersecurity and Infrastructure Security Agency (CISA) guidance. Refer to the [Secure by design](https://www.cisa.gov/sites/default/files/2023-10/SecureByDesign_1025_508c.pdf) and [Safe Software Deployment: How Software Manufacturers Can Ensure Reliability for Customers](https://www.cisa.gov/sites/default/files/2024-10/safe-software-deployment-how-software-manufacturers-can-ensure-reliability-for-customers-508c.pdf?form=MG0AV3) from CISA.

By diligently implementing these practices, you can contribute to the security and reliability of Windows systems that impact the lives of billions of people every day.

### Microsoft Virus Initiative

The Microsoft Virus Initiative (MVI) helps organizations improve the security solutions our customers rely on to keep them safe. We provide tools, resources, and knowledge to support better-together experiences with great performance, reliability, and compatibility. Microsoft collaborates with MVI partners to define and follow Safe Deployment Practices (SDP) to support the safety and resiliency of our mutual customers. If you are an antivirus vendor, see [Microsoft Virus Initiative](/defender-xdr/virus-initiative-criteria) to learn how to join MVI for more assistance on software deployment. To read more about Windows and security products, see this blog article by David Weston - [Windows Security best practices for integrating and managing security tools](https://www.microsoft.com/security/blog/2024/07/27/windows-security-best-practices-for-integrating-and-managing-security-tools/). It explains why security products use kernel-mode drivers today and the safety measures Windows provides for third-party solutions. In addition, it describes how to leverage the integrated security capabilities of Windows for increased security and reliability.

## Call to action 

To make your driver more secure and reliable, carefully follow the guidance provided in the following topics.


|Topic                    |Description|
|------------------------ |---------- |
| [Driver security checklist](driver-security-checklist.md) | A driver security checklist for Windows driver developers.|
| [Best practices for constraining high privileged behavior in kernel mode drivers](driver-security-dev-best-practices.md) | How to write secure code for Windows drivers to prevent abuse and tampering by malicious actors.|
| [Threat modeling for drivers](threat-modeling-for-drivers.md) | How to create and use a threat models for drivers.|
| [Windows security model for driver developers](windows-security-model.md) | How the Windows security model applies to drivers and explains what driver writers must do to improve the security of their code.|

If you are involved in developing a Windows driver, contribute to the security measures that have a significant impact on the lives of the billions of people who use Windows every day.
