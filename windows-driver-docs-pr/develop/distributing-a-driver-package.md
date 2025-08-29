---
title: Distributing a Driver Package
description: This topic describes distributing a driver package usingWindows Update - a robust, secure, globally scaled, regulatory compliant, distribution system that should be used.
ms.date: 01/14/2025
ms.topic: concept-article
---

# Distributing a driver package

This topic describes how to securely distribute your [driver package](/windows-hardware/drivers/install/driver-packages). It describes the advantages of distributing a driver package through Microsoft Windows Update (WU) and the complexity of creating your own distribution system. Windows Update provides a robust, secure, globally scaled, and regulatory compliant distribution system that should be used to deliver driver updates.

## Use Windows Update to distribute driver packages

Using Windows Update is strongly recommended for the distribution of driver packages. It offers many benefits including the following.

| Benefit               | Description  |
|---------------------- |------------  |
| Controlled distribution | A global infrastructure is managed 24 hours a day to safely and securely distribute drivers. | 
| Increased security | Driver packages distributed via Windows Update are signed, and the binaries are safely stored to decrease the risk of tampering or corruption. | 
| Known cost | Using Windows Update helps avoid unanticipated expenses that may come with establishing and managing an independent software distribution system. | 
| Regulatory compliance | Microsoft works to comply with all regulations, such as privacy, on a global basis. | 
| Customer satisfaction | Customers know that driver packages are tested and the reliability of their PC will not be impacted.  |

A well-designed software deployment process can deliver properly tested driver packages to users while minimizing the support costs and liability associated with Windows blue screen failures caused by a faulty driver update. 

### Preparing your driver package for Windows Update delivery

Windows Update has a number of systems in place to confirm that distributed driver packages are high quality and are created by a known, reliable, vendor.

The [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility/) is designed to help your company deliver systems, software and hardware products that are compatible with Windows and run reliably on Windows 10, Windows 11 and Windows Server 2022. The program also provides guidance for developing, testing and distributing drivers. Using the [Partner Center for Windows Hardware](/windows-hardware/drivers/dashboard/) dashboard, you can manage submissions, track the performance of your device or app, review telemetry and much more.

[Windows Hardware Quality Labs (WHQL) digitally signed](/windows-hardware/drivers/install/whql-release-signature) driver packages can be distributed through the Windows Update program. WHQL can digitally sign [Driver packages](/windows-hardware/drivers/install/driver-packages) that pass [Windows Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) testing. 

A WHQL release signature consists of a digitally-signed [catalog file](/windows-hardware/drivers/install/catalog-files). The digital signature does not change the driver binary files or the INF file that you submit for testing.

You can distribute a driver package through the Windows Update program if the driver package:

- Passes the [Windows Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) testing.

- Qualifies for the Windows Certification Program.

- Receives a [WHQL release signature](/windows-hardware/drivers/install/whql-release-signature).

- Meets additional requirements that ensure that Windows Update can determine the correct driver package for the user's device, can legally distribute it, and can automatically download it.

Because the requirements of the Windows Update program are frequently updated, you should regularly check [Windows Hardware Lab Kit](/windows-hardware/test/hlk/) for the latest information.

### Distribution safe software update procedures

All Windows Hardware Quality Labs (WHQL) signed driver packages are run through Microsoft’s ingestion checks and malware scans and must pass before being approved for signing. Installing signed driver packages allows for a smoother end user experience.

### Distribution security

One of the benefits of using Windows Update is that the servers, the transmission process, and the client logic that validates and applies the updates is a well-tested process that keeps over one billion PCs up to date. Many security experts that work at Microsoft are dedicated to maintaining the system against ever increasing, sophisticated, attacks.

### Controlled gradual update rollout

If a third-party vendor chooses to distribute their driver package via Windows Update, the driver package also goes through Microsoft’s flighting and [gradual rollout](/windows-hardware/drivers/dashboard/gradual-rollout) processes to observe quality and ensure the driver package meets the necessary quality criteria for a broad release.

Gradual rollout uses Windows telemetry to ensure your customers are having the best possible experience. Should a driver package appear unhealthy during gradual rollout phase, Microsoft may choose to pause the driver package distribution for investigation and/or seek appropriate remediation, including a Microsoft-initiated driver package cancellation (expiration). For more information on the critical use of distribution rings, see [Gradual rollout](/windows-hardware/drivers/dashboard/gradual-rollout).

### Field testing for specific vendor selected PCs

Before releasing a driver package, it is a requirement to test it on target PCs that will process the update and load the driver. Using a delivery system separate than the final distribution system can lead to errors. This additional process for early driver testing must be designed, created, and managed.

Hardware partners can test driver package update scenarios by publishing a driver package to Windows Update and using test distribution. Once published, IHVs/OEMs can configure their client systems to request these drivers by configuring a predefined registry key value. The testing registry key adds prerelease drivers to the list of production drivers offered by Windows Update. This method restricts prerelease drivers from being offered to the general public. For more information, see [Test distribution guidance to self-host desktop drivers](/windows-hardware/drivers/dashboard/publishing-for-test-distribution).

## Creating your own distribution system for Windows drivers

Re-creating the Windows Update system is not recommended, as it involves increased risk, significant development resources and costs which are difficult to estimate. Many security and reliability checks are built into the Windows Update process that would need to be designed, written, tested, and implemented globally at scale.

Creating a secure and regulatory compliant, global data pipeline to measure driver quality, may be the most difficult part of the Windows Update system to replicate. Most vendors would prefer to not hear about a driver package failure that causes widespread Windows outages via public news outlets or social media. A better approach is to have real time data to guide the deployment of the driver package and halt and roll back driver package updates that damage a customer's PC.

There can be significant cost in designing, deploying, and managing a driver distribution system. For a description of safe software deployment practices refer to the CISA [Safe Software Deployment: How Software Manufacturers Can Ensure Reliability for Customers](https://www.cisa.gov/sites/default/files/2024-10/safe-software-deployment-how-software-manufacturers-can-ensure-reliability-for-customers-508c.pdf).

Many Windows customers will only accept Microsoft signed drivers as a way of reducing their security exposure. Windows 10 in S mode requires driver signing. For more information, see [Windows 10 in S mode Driver Requirements](/windows-hardware/drivers/install/windows10sdriverrequirements) and [Driver Signing](/windows-hardware/drivers/install/driver-signing), [Windows Driver update management in Microsoft Intune](/mem/intune/protect/windows-driver-updates-overview) and [Microsoft recommended driver block rules](/windows/security/application-security/application-control/app-control-for-business/design/microsoft-recommended-driver-block-rules). 

### Controlling update rollout velocity using telemetry

Another element that would need to be created for your own distribution system is a way to throttle the speed of the rollout based on telemetry.

An important principle of a feature update rollout is to only update systems that data shows will have a good experience. Both human supervision and machine learning is used to select the systems that are offered updates first. If Windows Update detects that a system might have an issue, we will not offer the update until that issue is resolved.

Windows Update starts slowly – to prioritize the update reliability over rollout velocity. When a new feature update release is available, it is first made available to a small percentage of “seekers,” users who take action to get the updates early. Then telemetry is monitored carefully to learn about any new issues that may occur as more users receive the driver. This is done by watching telemetry, closely partnering with our customer service team to understand what customers report to us, analyzing feedback logs and screenshots directly through our Feedback Hub, and listening to automated summaries of signals sent through social media channels. If a combination of factors is found that results in a bad experience, a block is created that prevents similar devices from receiving an update until a full resolution occurs. Recreating this system would be a complex undertaking.

### Driver testing - flighting

Similar to a test flight of a new plane, [Driver flighting](/windows-hardware/drivers/dashboard/driver-flighting) in the [Partner Center for Windows Hardware](/windows-hardware/drivers/dashboard/) enables you to distribute your driver package within defined Windows Insider rings, while providing automatic monitoring and evaluation.  Upon a successful test flight and approval from Microsoft, the driver package is distributed publicly through Windows Update. A report of your driver package's performance will be generated after the completion of a flight, enabling you to evaluate its critical functionality and update scenarios.

To create your own distribution system, similar monitoring functionality must be duplicated.

### Driver quality measures

One of the most difficult to duplicate aspects of Windows Update is the driver package quality measures and real time data acquisition and processing. 78 trillion security signals are collected by Microsoft each day, using data that customers have chosen to share. This data pipeline is selectively harvested to gather actionable data for specific driver package updates.  Replicating this data pipeline is a large and complex undertaking. Customer privacy must be respected and in different areas of the world, such as the EU, where there are additional requirements for the gathering, storage, and use of customer data.

Using knowledge gained over many years, [Microsoft driver measures](/windows-hardware/drivers/dashboard/overview-of-microsoft-driver-measure-dictionary) have been developed, such as [Percent of Machines Without a Kernel Mode Crash](/windows-hardware/drivers/dashboard/pct-machines-without-kernel-mode-crash). Monitoring the correct data, in real time, is the only way to have a true measure of the health of a driver package update.

### Security Incident Response Plan (SIRP)

As the update system can be a significant target for cyber-attacks, it must be created to be secure. In addition, it must be monitored around the clock for possible intrusion or compromise. When an intrusion occurs, an appropriate response must be quickly developed and implemented by security experts. For more information about creating a Security Incident Response Plan (SIRP), see [Computer Security Incident Handling Guide](https://csrc.nist.gov/pubs/sp/800/61/r2/final) from NIST and [Incident Response Plan (IRP) Basics](https://www.cisa.gov/resources-tools/resources/incident-response-plan-irp-basics?form=MG0AV3) from CISA.


## Microsoft Virus Initiative

The Microsoft Virus Initiative (MVI) helps organizations improve the security solutions our customers rely on to keep them safe. We provide tools, resources, and knowledge to support better-together experiences with great performance, reliability, and compatibility. Microsoft collaborates with MVI partners to define and follow Safe Deployment Practices (SDP) to support the safety and resiliency of our mutual customers. 

If you are an anti-virus vendor, see [Microsoft Virus Initiative](/defender-xdr/virus-initiative-criteria) to learn how to join MVI for more assistance on software deployment.

For information on how security vendors can better leverage the integrated security capabilities of Windows for increased security and reliability, see [Windows Security best practices for integrating and managing security tools](https://www.microsoft.com/security/blog/2024/07/27/windows-security-best-practices-for-integrating-and-managing-security-tools).


## Additional resources

To learn more about secure by design principles and practices, visit CISA’s [Secure by Design](https://www.cisa.gov/securebydesign).

For information on the Cybersecurity Executive Order from the United States government, see [The Cybersecurity Executive Order: What’s Next for Federal Agencies?](https://www.microsoft.com/industry/microsoft-in-business/security/2021/06/17/the-cybersecurity-executive-order-whats-next-for-federal-agencies/).

For information on creating a Windows 11 deployment plan and other information about deploying Windows Updates, see [Create a deployment plan](/windows/deployment/update/create-deployment-plan).

For driver updates lessons learned in the Windows 10 era, see [Driver quality in the Windows ecosystem](https://blogs.windows.com/windowsexperience/2018/12/19/driver-quality-in-the-windows-ecosystem/).
