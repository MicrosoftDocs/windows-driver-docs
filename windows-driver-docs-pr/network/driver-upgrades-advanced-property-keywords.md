---
title: Advanced Properties Migration
description: How user state for advanced properties is migrated on driver upgrade
ms.assetid: 636b9eeb-7184-4c7a-8485-2b71603ea0ac
keywords: ["add-registry-sections WDK networking , Advanced properties page configuration", "Advanced properties page configuration WDK networking", "parameters WDK networking", "configuration parameters WDK networking", "upgrade", "update", "Windows Update", "migration"]
---

# Advanced Properties Migration

Because [advanced properties](specifying-configuration-parameters-for-the-advanced-properties-page.md) contain user specified state, that user state must be preserved on driver upgrades and after Windows updates. This is to align with user expectations that their settings are permanent. As of Windows 10 Creator's Update (1703), user state will always be preserved for registry values that a driver specifies as being advanced keywords. This is a break from previous versions of Windows that would always re-configure the INF on-top of user state.

Resetting user state after a driver or Windows update breaks user's expectations. That's why it's important to manage this state carefully. If a driver needs to reset an advanced property on upgrade, the driver should detect the first time a driver is started after upgrade and perform the reset in code, but it should only perform the reset exactly once and allow the user to continue to configure the driver to their liking.

It is recommended to mark any advanced properties in the INF where the default may change in the future as "Optional". This gives the driver the freedom to re-interpret the default behavior in the future, while only falling back to the old default for users that explicitly configured the property.
