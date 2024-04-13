---
title: RunAs
description: RunAs
ms.date: 04/20/2017
---

# RunAs

TAEF provides a mechanism to execute tests Elevated, Restricted, as Local System or within a Low Integrity process.

## Prerequisites

- [Te.Service](te-service.md) must be installed and running on the machine in order to run elevated tests from a non-elevated process, run non-elevated tests from an elevated process, or to run tests as Local System.

## RunAs Types

TAEF supports the following RunAs types, which are specified via test metadata or the command prompt.

- [RunAs Elevated](runas-elevated.md)
- [RunAs LowIL](runas-lowil.md)
- [RunAs Restricted](runas-restricted.md)
- [RunAs System](runas-system.md)
