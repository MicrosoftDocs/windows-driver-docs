---
title: Creating a Service Provider for a SAN
description: Creating a Service Provider for a SAN
ms.assetid: 848b6fd5-64f8-4e62-9c54-c23bbc3d9ede
keywords:
- Windows Sockets Direct WDK , service providers
- SAN service providers WDK , creating
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Service Provider for a SAN





This section provides a brief description of the functions that make up the interface between a SAN service provider DLL and the Windows Sockets switch. The SAN service provider DLL exports a single entry point for its initialization function [**WSPStartupEx**](https://msdn.microsoft.com/library/windows/hardware/ff566321). The SAN service provider's **WSPStartupEx** function in turn makes most of the other interface functions accessible to the Windows Sockets switch through a dispatch table. The remaining interface functions are supplied to the switch through calls to the SAN service provider's [**WSPIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff566296) function. The interface functions include [Windows Sockets SPI functions](windows-sockets-spi-functions-required-for-sans.md) and [SAN-specific extensions to the Windows Sockets SPI interface](windows-sockets-spi-extensions-for-sans.md).

The [Windows Sockets Direct reference](https://msdn.microsoft.com/library/windows/hardware/ff565857) provides detailed information about these functions as implemented in a SAN service provider. Do not use the Microsoft Windows SDK descriptions of the Windows Sockets SPI functions. The Windows SDK descriptions do not contain SAN-specific requirements.

This section also lists the [Windows Sockets SPI functions that a SAN service provider is not required to supply](windows-sockets-spi-functions-not-required-for-sans.md).

 

 





