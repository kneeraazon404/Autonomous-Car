# Autonomous Vehicle System: Perception, Decision-Making, and Dynamics

![Autonomous Vehicle Concept]
*Example: Autonomous vehicle perception and control pipeline.*

A comprehensive repository for understanding the technical components of autonomous vehicles, including **environment perception**, **decision-making**, **vehicle dynamics**, and **safety assurance**. This project aligns with SAE automation levels (0–5) and integrates key research on kinetic/dynamic modeling, ODD, and OEDR.

---

## Table of Contents
- [SAE Levels of Automation](#sae-levels-of-automation)
- [Technical Components](#technical-components)
  - [Perception](#perception)
  - [Decision-Making](#decision-making)
  - [Vehicle Dynamics](#vehicle-dynamics)
  - [Safety Assurance](#safety-assurance)
- [Operational Design Domain (ODD)](#operational-design-domain-odd)
- [References](#references)
- [Contributing](#contributing)

---

## SAE Levels of Automation
| Level | Description | Key Capabilities |
|-------|-------------|------------------|
| **0** | No Automation | Human controls all tasks. |
| **1** | Longitudinal **or** Lateral Control | Assistive systems (e.g., adaptive cruise control). |
| **2** | Combined Longitudinal/Lateral Control | Partial automation (e.g., Tesla Autopilot). |
| **3** | Conditional Automation | OEDR* for limited scenarios (e.g., traffic jam assist). |
| **4** | High Automation | Full OEDR in defined ODD; handles emergencies. |
| **5** | Full Automation | Unrestricted ODD; no human intervention required. |

*OEDR: Object/Event Detection & Response

---

## Technical Components

### Perception
- **Objective**: Interpret environment via sensors (LiDAR, cameras, radar).
- **Dataset**: [KITTI Vision Benchmark Suite](http://www.cvlibs.net/datasets/kitti/) for 3D object detection.
- **Key Models**: Semantic segmentation, SLAM, sensor fusion.

### Decision-Making
- **Requirements**: Path planning, risk assessment, real-time response.
- **Algorithms**: Markov Decision Processes (MDPs), Reinforcement Learning (RL).

### Vehicle Dynamics
#### Longitudinal Dynamics
- Throttle/brake control for speed regulation.  
  **Resource**: [Longitudinal Vehicle Dynamics (Springer)](https://link.springer.com/chapter/10.1007%2F978-1-4614-1433-9_4)

#### Lateral Dynamics
- Steering control using bicycle models.  
  **Resource**: [Lateral Dynamics of Bicycle Model](https://example.com/lateral-dynamics)  
  **Advanced**: [Linear Tire Model with Varying Parameters](https://hal.archives-ouvertes.fr/hal-01690792/document)

#### 2D/Kinetic Modeling
- [Dynamic 2D Modeling (Chalmers)](http://publications.lib.chalmers.se/records/fulltext/244369/244369.pdf)  
- [Kinetic Modeling Primer](https://example.com/kinetic-modeling)

### Safety Assurance
- **Key Study**: [Driving to Safety (RAND Corporation)](https://rand.org/pubs/research_reports/RR1478.html)  
- **Focus**: Risk quantification, fail-safe mechanisms, validation frameworks.

---

## Operational Design Domain (ODD)
Defines the conditions under which the autonomous system operates:
- **Geographic**: Urban vs. highway.
- **Environmental**: Weather, lighting.
- **Traffic**: Density, road types.
- **Speed Limits**: Operational thresholds.

---

## References
1. KITTI Dataset: http://www.cvlibs.net/datasets/kitti/
2. Vehicle Dynamics Models: [Springer](https://link.springer.com), [Chalmers](http://publications.lib.chalmers.se)
3. Safety Framework: [RAND Study](https://rand.org/pubs/research_reports/RR1478.html)

---

## Contributing
Contributions are welcome!  
1. Fork the repository.  
2. Submit a PR with clear documentation/testing.  
3. Adhere to [SAE J3016](https://www.sae.org/standards/content/j3016_202104/) standards for automation levels.
