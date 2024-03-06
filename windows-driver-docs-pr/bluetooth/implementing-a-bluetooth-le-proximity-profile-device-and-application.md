---
title: Bluetooth LE Proximity Profile Overview
description: Proximity detection is a common use of Bluetooth Low Energy (LE).
ms.date: 01/10/2024
---

# Bluetooth LE Proximity Profile overview

Proximity detection is a common use of Bluetooth Low Energy (LE). This section provides guidelines to create a device implementation of the Proximity Profile that you can use to develop a UWP device app.

Before you develop this app, you should be familiar with Bluetooth LE functions and the Bluetooth LE Proximity profile specification.

## Example service declaration

Bluetooth Low Energy introduced a new physical layer that shares the same frequency space as Bluetooth Basic Rate. Low energy profiles are organized into what's called the Generic Attribute Profile (or GATT).

A GATT profile declares one or more services that define a use case or scenario. To develop a compliant service implementation, you must organize *characteristics* so that they conform to the established schema defined on the [Bluetooth Special Interest Group (SIG) developer website](https://www.bluetooth.com/develop-with-bluetooth/).

This diagram shows how *characteristics* are structured inside a typical GATT service.

:::image type="content" source="images/bthleservicedeclaration.png" alt-text="Diagram that shows a typical GATT service declaration with characteristics.":::

An example proximity profile is described further in [Bluetooth Proximity Profile](bluetooth-proximity-profile.md).
