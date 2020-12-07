---
title: Mobile Plans Integration
description: This topic describes the Integration step for the Mobile Plans program.
keywords:
- Windows Mobile Plans Integration, Mobile Plans integration mobile operators
ms.date: 03/25/2019
ms.localizationpriority: medium
---

# Mobile Plans Integration

## Overview

This topic describes what steps are needed to integrate and validate the mobile operator implementation of the Mobile Plans solution.

## Mobile Plans service environments

There are two Mobile Plans service environments, *Staging* and *Production*. The integration and validation will be performed in the *staging* environment, while the *production* environment is only used for commercial launch.

## Validation

This section describes testing and validation that you must do to ensure that you are ready to move into the Integration phase.

### Mobile Operator web portal

Validate that you can run 50 end-to-end user cases that you defined. For example:

- Install an eSIM profile.
- Activate a warm SIM.
- Add balance to your subscription.
- Canceling a transaction.

### Walled Garden

When the user has no balance, ensure that the user can access Walled Garden sites defined in [Walled Garden](mobile-plans-walled-garden.md).

### Getting Balance

1. When the user is in the Walled Garden state, the balance returned must be zero.
2. As the user consumes data, the balance returned must decrement to reflect the data remaining.
3. As the allotted time lapses after the `Create Order` API has been invoked, the time remaining must decrement to reflect the time remaining.

### Test with expired MTLS certificate

1. Validate MO APIs without the MTLS certificate. Expected Status: 401 Unauthorized.
2. Validate with an expired MTLS certificate. Expected Status: 401 Unauthorized.

### GetBalance negative tests

1. Validate with an invalid SIM. Expected Status: 404 Not Found.
2. Validate with unknown location or bad location string/number. Expected Status: 400 (Bad Request).
3. Validate with filter limit as a negative number and exceeding the limit of an INT. Expected Status: 400 - Bad Request. Expected Status 200 OK for filter limit (integer).
4. Validate a call to `GetBalance` without any *location* (or empty location), *fieldTemplate*, *limit*, and many more combinations of parameters. Expected Status: 400 (Bad Request) with any bad parameter’s value. Expected Status 200 – OK.

### GetBalance API load test

Before the `GetBalance` API is enabled in production, both Mobile Plans services and mobile operator services should be tested to see if they can handle the projected load. The mobile operator is expected to run a load test. Once that has passed, Mobile Plans executes a load test. The mobile operator should provide a list of 1000 ICCIDs that are temporally used in the load test.

This test configuration is generated from projected traffic of 10,000 SIMs. The Peak RPS is calculated based on 3 times this traffic projection.

- Load tests will be executed from 25 test agents.
- Load tests will execute for:
  - 1 hour with 1000 different users (#ICCIDs) with 3 RPS (Peak).
- The load distribution cross APIs would be as follows:

| API | Load distribution | Expected RPS | Peak RPS |
| --- | --- | --- | --- |
| GetBalance | 96% | 1 | 3 |

During test runs, the expected success rate is: **99.9%** and average latency: **400ms**. On achieving this success rate, the MO API will be ready to enable in the Mobile Plans production service.
