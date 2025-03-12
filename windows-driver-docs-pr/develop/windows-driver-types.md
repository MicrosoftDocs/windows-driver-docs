---
title: Windows Driver Types
description: Learn the types of Windows drivers, including Desktop, Universal, and Windows drivers. Understand the importance of DCH design principles, driver package isolation, and API layering for enhanced reliability and future certification.
ms.date: 03/12/2025
ai-usage: ai-assisted
---

# Windows driver types

When developing a driver for the Windows operating system, you have three types of drivers to choose from:

1. **Desktop driver**: This type of driver is designed to run exclusively on Windows desktop editions.

1. **Universal driver**: Universal drivers are designed to be compatible across various Windows platforms. If your driver passes the `infverif /u` and [ApiValidator](./validating-windows-drivers.md#apivalidator) checks, you can create a Universal Driver. For more info, refer to [Using a Universal INF File](../install/using-a-universal-inf-file.md).

1. **Windows driver**: To create a Windows driver that runs on both desktop and non-desktop variants of Windows, your driver must pass the `infverif /w` check, which includes [Driver Package Isolation](../develop/driver-isolation.md).

For information on configuring your build settings, see [Target Platforms](./target-platforms.md).

## Extra requirements for Windows drivers

To ensure your Windows driver meets the necessary standards, it must comply with the following requirements:

- Adhere to the [DCH Design Principles and Best Practices](dch-principles-best-practices.md). DCH (declarative, componentized, hardware support apps) is a set of design principles that ensures drivers are more reliable, secure, and easier to maintain. By following DCH principles, you can create drivers that are modular and can be updated independently of the operating system, enhancing overall system stability and performance.

- Follow the guidelines for [Driver Package Isolation](driver-isolation.md). Driver package isolation ensures that each driver operates within its own isolated environment, reducing the risk of conflicts with other drivers and enhancing system stability. This isolation helps in diagnosing and resolving issues more efficiently, as problems can be traced back to individual drivers without affecting the entire system.

- **API layering requirements**: Ensure your driver meets the [API Layering Requirements](api-layering.md). API layering involves structuring your driver to interact with the operating system through well-defined layers of APIs. This approach promotes modularity and maintainability, making it easier to update or replace individual components without affecting the entire driver. It also enhances compatibility and reduces the risk of introducing bugs when changes are made.

## Benefits of meeting Universal and Windows driver standards

While it isn't mandatory for a driver running solely on Windows desktop to meet the extra requirements for a Universal Driver or Windows Driver, doing so offers several advantages:

- **Enhanced serviceability**: Improved ease of maintenance and updates.
- **Increased reliability**: Greater stability and performance.
- **Future certification**: Prepares your driver for potential future certification on non-desktop variants of Windows.

By adhering to these standards, you ensure your driver is robust, versatile, and ready for future developments in the Windows ecosystem.

## See also

- [DCH Design Principles and Best Practices](./dch-principles-best-practices.md)
- [ApiValidator](./validating-windows-drivers.md#apivalidator)
- [Using a Universal INF File](../install/using-a-universal-inf-file.md)
- [Driver Package Isolation](../develop/driver-isolation.md)
- [Target Platforms](./target-platforms.md)
- [API Layering Requirements](api-layering.md)
