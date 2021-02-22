---
title: Validating driver updates for Modern Standby systems
description: This topic describes how to validate driver updates that target Modern Standby systems.
ms.topic: article
ms.date: 12/17/2020
ms.localizationpriority: medium
---

# Validating driver updates for Modern Standby systems 

When a driver update will be released to [Modern Standby](/windows-hardware/design/device-experiences/modern-standby-basic-test-scenarios) systems, it is critical to ensure that the driver’s power management is compatible with Modern Standby and does not negatively impact battery life for mobile form factor systems or power efficiency for desktop form factor systems. 

If the driver update is targeting Modern Standby systems, all tests and validation must be performed on at least one [system supporting Modern Standby](/windows-hardware/design/device-experiences/overview-of-modern-standby-validation#verifying-if-a-system-is-modern-standby-capable). This should include any HLK tests or other test suites typically used to validate a particular driver update. 

Testing on a variety of Modern Standby systems and OS releases is recommended, as power management and battery life are impacted by the combination of hardware, firmware, drivers and the OS. If the driver update is also targeting Traditional Sleep (S3) systems, validation should be performed on at least one, and preferably a variety, of S3 systems as well. 

Before installing the updated driver, the system’s stability should be confirmed by running the HLK test suite, i.e. the HLK playlist automatically generated on the test system. If the existing version of the driver is causing a failure(s), the corresponding device can be temporarily disabled via Device Manager before rerunning the HLK test suite. Disabling the device may cause some HLK test failures, such as failing to meet DRIPS requirements in the Modern Standby Basic Requirement Test or failing the DFx System Verification Test; however, the remainder of the test results should indicate whether the platform is generally stable and able to enter and exit Modern Standby. Once system stability has been confirmed, the disabled device can be re-enabled via Device Manager and the updated driver installed. 

With the updated driver installed, the system must pass the HLK [Modern Standby Basic Requirement Test on AC](/windows-hardware/test/hlk/testref/c0c51f07-5b17-4b26-a7ce-bfc9e7611dac) and [DC power](/windows-hardware/test/hlk/testref/c0c51f07-5b17-4b26-a7ce-bfc9e7611ddc) to verify that the system is still able to enter a low power state and resume from standby quickly. Modern Standby systems are required to pass these tests prior to shipping, so it is crucial to ensure that the driver update does not cause regressions. It is recommended to perform a hibernate transition on the system before executing this test.

The system must also pass the [Directed PoFx (DFx) System Verification Test](/windows-hardware/test/hlk/testref/def16163-9118-4d4a-b559-37873befa12e), which validates that devices on the system that are required to support DFx have the requisite support in their drivers. It is important to verify that DFx support has not been removed from a device that requires it in a driver update. for more information on DFx, please refer to [Introduction to the Directed Power Management Framework](../kernel/introduction-to-the-directed-power-management-framework.md). It is recommended to perform a hibernate transition on the system before executing this test.

Next, the system must pass the [Device Fundamentals Tests](../devtest/device-fundamentals-tests.md). After all aforementioned tests have been run, the system must pass the HLK [Runtime Power Focused Stress with Driver Verifier's Concurrency Stress test](/windows-hardware/test/hlk/testref/dfa7f945-7b63-4693-a555-0f38f33c971c) and [Modern Standby Stress with Driver Verifier’s Concurrency Stress test](/windows-hardware/test/hlk/testref/ae264d13-307b-452b-b5fc-4d9098ea22f1) to confirm that the system can undergo runtime power management transitions and Modern Standby transitions after device I/O without error.