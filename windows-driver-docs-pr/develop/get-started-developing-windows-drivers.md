---
title: Get Started Developing Windows Drivers
description: Learn how to develop Windows drivers, including Desktop, Universal, and Windows Drivers. Understand the importance of DCH Design Principles, Driver Package Isolation, and API Layering for enhanced reliability and future certification.
ms.date: 09/09/2024
ai-usage: ai-assisted
---

# Get started developing Windows drivers

When developing a driver for the Windows operating system, you have three main options to choose from:

1. **Desktop Driver**: This type of driver is designed to run exclusively on Windows Desktop editions.

1. **Universal Driver**: Universal Drivers are designed to be compatible across various Windows platforms. If your driver passes the `infverif /u` and [ApiValidator](./validating-windows-drivers.md#apivalidator) checks, you can create a Universal Driver. For more info, refer to [Using a Universal INF File](../install/using-a-universal-inf-file.md).

1. **Windows Driver**: To create a Windows Driver that runs on both Desktop and non-Desktop variants of Windows, your driver must pass the `infverif /w` check, which includes [Driver Package Isolation](../develop/driver-isolation.md).

For information on configuring your build settings, see [Target Platforms](./target-platforms.md).

## Extra requirements for Windows Drivers

To ensure your Windows Driver meets the necessary standards, it must comply with the following requirements:

- Adhere to the [DCH Design Principles](dch-principles-best-practices.md). DCH (Declarative, Componentized, Hardware Support Apps) is a set of design principles that ensures drivers are more reliable, secure, and easier to maintain. By following DCH principles, you can create drivers that are modular and can be updated independently of the operating system, enhancing overall system stability and performance.

- Follow the guidelines for [Driver Package Isolation](driver-isolation.md). Driver Package Isolation ensures that each driver operates within its own isolated environment, reducing the risk of conflicts with other drivers and enhancing system stability. This isolation helps in diagnosing and resolving issues more efficiently, as problems can be traced back to individual drivers without affecting the entire system.

- **API Layering Requirements**: Ensure your driver meets the [API Layering Requirements](api-layering.md). API Layering involves structuring your driver to interact with the operating system through well-defined layers of APIs. This approach promotes modularity and maintainability, making it easier to update or replace individual components without affecting the entire driver. It also enhances compatibility and reduces the risk of introducing bugs when changes are made.

## Benefits of meeting Universal and Windows Driver standards

While it isn't mandatory for a driver running solely on Windows Desktop to meet the extra requirements for a Universal Driver or Windows Driver, doing so offers several advantages:

- **Enhanced Serviceability**: Improved ease of maintenance and updates.
- **Increased Reliability**: Greater stability and performance.
- **Future Certification**: Prepares your driver for potential future certification on non-Desktop variants of Windows.

By adhering to these standards, you can ensure your driver is robust, versatile, and ready for future developments in the Windows ecosystem.
