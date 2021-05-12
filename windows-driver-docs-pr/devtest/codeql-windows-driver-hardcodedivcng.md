---
title: HardcodedIVCNG(Supplemental Windows Driver CodeQL Query)
description: HardcodedIVCNG a Supplemental Windows Driver CodeQL Query
ms.date: 01/11/2021
ms.localizationpriority: medium
---

# HardcodedIVCNG (Windows Driver CodeQL Query)

## Overview

An initialization vector (IV) is an input to a cryptographic primitive being used to provide the initial state. The IV is typically required to be random or pseudorandom (randomized scheme), but sometimes an IV only needs to be unpredictable or unique (stateful scheme).

Randomization is crucial for some encryption schemes to achieve semantic security, a property whereby repeated usage of the scheme under the same key does not allow an attacker to infer relationships between (potentially similar) segments of the encrypted message.

## Recommendation

All symmetric block ciphers must also be used with an appropriate initialization vector (IV) according to the mode of operation being used.

If using a randomized scheme such as CBC, it is recommended to use cryptographically secure pseudorandom number generator such as [BCryptGenRandom](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom).

## Additional Details

This query can be found in the [Microsoft GitHub CodeQL repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools).  See the [CodeQL and the Static Tools Logo Test](./static-tools-and-codeql.md) page for details on how Windows Driver developers can download and run CodeQL.

## Additional References:

- [BCryptEncrypt function (bcrypt.h)](/windows/win32/api/bcrypt/nf-bcrypt-bcryptencrypt)
- [BCryptGenRandom function (bcrypt.h)](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom)
- [Initialization vector (Wikipedia)](https://en.wikipedia.org/wiki/Initialization_vector)
