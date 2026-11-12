---
title: Windows Driver Quality Initiative
description: Learn about the Driver Quality Initiative (DQI), an ecosystem-wide effort to raise the quality, reliability, and security of Windows drivers.
ms.date: 11/12/2026
ms.topic: concept-article
ai-usage: ai-assisted
#customer intent: As a driver developer or device maker, I want to understand the Driver Quality Initiative (DQI) so that I can align my drivers with its four pillars.
---

# What is the Driver Quality Initiative (DQI)?

The Driver Quality Initiative (DQI) is an ongoing, ecosystem-wide effort by Microsoft and its hardware partners to raise the quality, reliability, and security of drivers across Windows. If you build, ship, or manage Windows drivers, DQI affects the requirements, tools, and quality signals that you work with. This article explains why driver quality matters, describes the four DQI pillars, and links to guidance that helps you align your drivers with each pillar.

## Why driver quality matters

Drivers connect Windows to the silicon, components, and peripherals in every Windows device. Thousands of partners contribute to tens of thousands of active driver families across the Windows install base.

When drivers are high quality, customers get reliable, secure, and performant devices. When a driver fails, customers experience it as a device problem, regardless of where the root cause is.

Raising the bar on driver quality takes coordinated work across the ecosystem. Through DQI, Microsoft builds the frameworks, tools, and quality signals, and works with partners to raise driver quality so that customers can rely on their Windows devices from day one through the full life of the PC.

Microsoft introduced DQI at the Windows Hardware Engineering Conference (WinHEC) in May 2026. DQI builds on the learnings and infrastructure of the [Windows Resiliency Initiative (WRI)](https://blogs.windows.com/windowsexperience/2024/11/19/windows-security-and-resiliency-protecting-your-business/).

## DQI pillars

DQI is organized around four pillars:

| Pillar | Goal | Focus |
|--------|------|-------|
| :::image type="icon" source="images/driver-quality-initiative-architecture.svg" border="false"::: [Architecture](#architecture-secure-by-design) | Secure by design | Harden kernel-mode drivers, and move functionality to user mode or to Microsoft class drivers where it makes sense. |
| :::image type="icon" source="images/driver-quality-initiative-trust.svg" border="false"::: [Trust](#trust-verified-and-certified) | Verified and certified | Raise the bar for trusted partners and trusted drivers. |
| :::image type="icon" source="images/driver-quality-initiative-lifecycle.svg" border="false"::: [Lifecycle](#lifecycle-secure-and-reliable) | Secure and reliable | Improve how drivers are published, maintained, updated, and retired. |
| :::image type="icon" source="images/driver-quality-initiative-quality-measures.svg" border="false"::: [Quality measures](#quality-measures-quality-quantified) | Quality quantified | Measure driver quality beyond crashes. |

## Architecture: Secure by design

Code that runs in kernel mode shares a single address space with the operating system, so a bug in a kernel-mode driver can crash the whole system or expose a security vulnerability. Through DQI, Microsoft is hardening kernel-mode drivers and helping partners move third-party kernel-mode drivers to user-mode drivers or to Microsoft-authored class drivers. This transition improves driver security, reliability, and resiliency.

Current investments include:

- **User-mode drivers**: Performance improvements for PCIe devices that use direct memory access (DMA).
- **Class drivers**: SoundWire Device Class for Audio (SDCA), a new I3C class driver, the USB Network Control Model (NCM) Ethernet class driver, and continued improvements to existing Microsoft class drivers in Windows 11.

To align your drivers with this pillar:

- Use a Microsoft-provided class driver when one supports your device. For example, see [USB device class drivers included in Windows](usbcon/supported-usb-classes.md).
- If you need to write a driver, consider a user-mode driver. See [Choose a driver model](gettingstarted/choosing-a-driver-model.md), [User mode and kernel mode](gettingstarted/user-mode-and-kernel-mode.md), and [Getting started with UMDF](wdf/getting-started-with-umdf-version-2.md).
- If your driver must run in kernel mode, follow the [Driver security checklist](driversecurity/driver-security-checklist.md), [implement memory integrity compatible code](driversecurity/implement-hvci-compatible-code.md), and meet the [driver package isolation](develop/driver-isolation.md) requirements.

## Trust: Verified and certified

Through DQI, Microsoft is raising the bar for trusted partners and trusted drivers. Investments include:

- Stronger partner verification.
- Expanded automated analysis of drivers, including vulnerability scanning.
- Updated [Windows Hardware Compatibility Program (WHCP)](/windows-hardware/design/compatibility/whcp-specifications-policies) requirements.

To align your drivers with this pillar:

- Analyze your driver before you submit it. See [CodeQL and the Static Tools Logo Test](devtest/codeql-overview.md) and [Analyzing a driver using code analysis and verification tools](develop/analyzing-driver-quality-by-using-code-analysis-tools.md).
- Review the [driver security guidance](driversecurity/index.md).
- Test your driver with the [Windows Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/), and meet the [driver code signing requirements](dashboard/code-signing-reqs.md).

## Lifecycle: Secure and reliable

Through DQI, Microsoft is improving how it manages drivers across their full lifecycle. Investments include:

- Better Windows Update catalog hygiene, including deprecating outdated or low-quality drivers.
- Advancing software bill of materials (SBOM) alignment.
- Faster issue analysis through driver symbols.
- More precise driver targeting, and faster recovery when a problematic driver reaches devices.

To align your drivers with this pillar:

- Target your drivers precisely when you [publish a driver to Windows Update](dashboard/publish-a-driver-to-windows-update.md). To target specific systems, see [Using Computer Hardware IDs (CHIDs)](dashboard/using-chids.md).
- Use [driver flighting](dashboard/driver-flighting.md) to validate drivers with a limited audience before broad release.
- [Expire a driver from Windows Update](dashboard/expire-a-driver-from-windows-update.md) when it's outdated or replaced.

## Quality measures: Quality quantified

Through DQI, Microsoft is expanding how it measures driver quality beyond crashes to include stability, functionality, performance, power and thermal impact, and security. These measures give partners clearer signals about how their drivers affect the real customer experience.

To align your drivers with this pillar, monitor the quality measures for your drivers in Partner Center. See [Overview of the Microsoft driver measures](dashboard/overview-of-microsoft-driver-measure-dictionary.md).

## Who DQI is for

DQI raises the bar for drivers on every Windows device, so it matters to everyone who builds, manages, or uses Windows.

| Audience | What DQI means for you |
|----------|------------------------|
| **Driver developers**<br>Silicon partners and independent hardware vendors (IHVs) | Clearer requirements, tools, and quality signals for building secure and reliable drivers. Focus on the [Architecture](#architecture-secure-by-design) and [Trust](#trust-verified-and-certified) pillars. |
| **Device makers**<br>Original equipment manufacturers (OEMs) and original design manufacturers (ODMs) | More precise driver targeting, so the highest-quality driver reaches each of your devices through Windows Update. Focus on the [Lifecycle](#lifecycle-secure-and-reliable) and [Quality measures](#quality-measures-quality-quantified) pillars. |
| **IT pros and administrators** | More secure and reliable drivers across the devices you deploy and manage, and fewer outdated or low-quality drivers in Windows Update. To control driver updates for your organization, see [Manage Windows driver updates in Intune](/intune/device-updates/windows/manage-driver-updates). To block known vulnerable drivers, see [Microsoft recommended driver block rules](/windows/security/application-security/application-control/app-control-for-business/design/microsoft-recommended-driver-block-rules). |
| **Everyone who uses Windows** | Secure and reliable drivers from day one through the full life of your PC, whether you use it for school, work, creative projects, or gaming. To get the latest drivers, keep Windows up to date. |

## Stay up to date

The [WinHEC Online blog](https://techcommunity.microsoft.com/category/winhec-online/blog/winhec-online-blog) brings together the most important updates for the Windows driver ecosystem, including DQI progress: what shipped, what's changing, what's coming next, and what it means for partners. For technical details, also follow these blogs:

- [Hardware Dev Center blog](https://techcommunity.microsoft.com/category/winhec-online/blog/hardware-dev-center)
- [Windows Driver Developer blog](https://techcommunity.microsoft.com/category/windows/blog/windowsdriverdev)
- [Windows Hardware Certification blog](https://techcommunity.microsoft.com/category/winhec-online/blog/windows-hardware-certification)

## Next steps

To start aligning your drivers with DQI:

- Review the [driver security guidance](driversecurity/index.md).
- Learn how to manage your drivers in [Partner Center for Windows Hardware](dashboard/index.md).
- Check the latest [Windows Hardware Compatibility Program specifications and policies](/windows-hardware/design/compatibility/whcp-specifications-policies).

## Related content

- [Raising the bar together: Introducing the Driver Quality Initiative at WinHEC 2026](https://blogs.windows.com/windowsexperience/2026/05/14/raising-the-bar-together-introducing-the-driver-quality-initiative-at-winhec-2026/)
- [Welcome to WinHEC Online](https://techcommunity.microsoft.com/blog/winhec-online-blog/welcome-to-winhec-online/4552413)
