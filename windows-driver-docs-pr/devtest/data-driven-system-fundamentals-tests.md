---
title: Data-driven System Fundamentals tests
description: Overview of the System Fundamentals tests and associated utilities for Windows drivers
keywords:
- Sysfund tests
- data-driven tests
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Data-driven System Fundamentals tests
Starting with Enterprise WDK (EWDK) 1703, Microsoft provides configurable command-line versions of the System Fundamentals tests and associated utilities.  These are known as “data-driven” tests and utilities.
The data-driven System Fundamentals (SysFund) tests are configurable and customizable via an XML file (wdtftest.xml), and run via the command line. The tests are designed to run early and often during driver and device development.
Since the data-driven SysFund tests are functionally identical to the SysFund tests in the HLK, if a system can pass the data-driven SysFund tests, it should also be able to pass the HLK SysFund tests. Unlike the SysFund tests in the HLK, however, the data-driven SysFund tests are configurable to target a set of devices from one device to all devices on the system.  This allows for an iterative testing process for new or updated devices and systems.
