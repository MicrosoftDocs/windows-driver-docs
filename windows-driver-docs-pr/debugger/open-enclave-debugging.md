---
title: Open Enclave debugging
description: Open Enclave debugging
ms.date: 08/06/2020
---

# Open Enclave debugging

WinDbg version 1.0.1908.30002 and later supports Open Enclave debugging. Open Enclave applications utilize Hardware-based Trusted Execution Environments, also known as enclaves. An enclave is a protected memory region that provides confidentiality for data and code execution. It is an instance of a Trusted Execution Environment (TEE) which is usually secured by hardware, for example, [Intel Software Guard Extensions (SGX)](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions.html).

The Open Enclave SDK is a hardware-agnostic open source library for developing applications that utilize enclaves. For more information, see the project GitHub at https://github.com/openenclave/openenclave.

For information on how to debug Open Enclave applications using WinDbg, see [Debugging ELF Enclaves Using WinDbg](https://github.com/openenclave/openenclave/blob/master/docs/GettingStartedDocs/Windows_windbg.md).

## debugrt DLL

Some of the debugging functionality for Open Enclave is provided by the debugrt DLL that is loaded as part of the enclave debugging target. For more information and the source code, see the debugrt project GitHub https://aka.ms/debugrt.
