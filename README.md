#  Oncology RWE Line of Therapy (LOT) Engine

### *Deterministic Mapping for Integrated Evidence Generation (IEG)*

The `oncology-rwe-lot-engine` is a specialized Python framework designed to transform longitudinal Real-World Data (RWD) into clinically meaningful **Lines of Therapy (LOT)**. As shown in the repository overview (**{40BCB008-E7C5-4376-8865-062E6419E3A0}.png**), this tool supports HEOR and Medical Affairs teams in calculating key oncology metrics like **TTNT (Time to Next Treatment)** and therapy sequencing.


##  The Strategic Problem: Clinical Complexity in RWD

Mapping lines of therapy in oncology is notoriously difficult due to drug combinations, maintenance therapy, and treatment gaps. This engine provides a **standardized, deterministic logic** to ensure consistency across HTA submissions and peer-reviewed publications.

### Key Capabilities

* **LOT Mapping:** Automatically groups drug administration events into $1^{st}$, $2^{nd}$, and $3^{rd}$ lines of therapy based on oncology-specific business rules (e.g., 28-day gap rules, drug additions, and regimen switches).
* **TTNT Calculation:** As seen in `calculate_ttnt.py`, the engine measures the durability of treatment by calculating the interval between therapy starts.
* **Synthetic Oncology RWD:** Includes a generator (`generate_oncology_rwd.py`) that produces realistic, HIPAA-compliant patient journeys for testing and validation.


##  Project Structure & Modules

Referencing the file structure in **{40BCB008-E7C5-4376-8865-062E6419E3A0}.png**:

* **`lot_mapper.py`**: The core logic engine. Handles regimen identification and line-advancement triggers.
* **`calculate_ttnt.py`**: Analytical module for calculating "Time to Next Treatment"—a critical proxy for Progression-Free Survival (PFS) in RWE studies.
* **`generate_oncology_rwd.py`**: A data simulation tool that mimics oncology electronic health records (EHR) and claims data.


## Use Cases for Life Sciences

* **HEOR & HTA Submissions:** Provide transparent, reproducible LOT mapping for NICE, IQWiG, or ICER submissions.
* **Competitive Intelligence:** Analyze therapy sequencing (e.g., "What do patients take after failing a PD-1 inhibitor?") to inform commercial strategy.
* **Medical Affairs:** Generate real-world evidence on the "Unmet Need" in later lines of therapy.

## Technical Setup

```bash
# Clone the RWE Engine
git clone https://github.com/your-username/oncology-rwe-lot-engine.git
cd oncology-rwe-lot-engine

# Generate sample oncology data and map LOT
python generate_oncology_rwd.py
python lot_mapper.py

```

##  Integration with the "Precision-Patient-360" Suite

This engine provides the foundational clinical data used by the rest of the stack:

1. **Oncology-RWE-LOT-Engine:** (This Repo) Maps the clinical journey and therapy lines.
2. **[Cgt-Precision-Patient-360](https://www.google.com/search?q=link):** Uses mapped LOT to find patients who have "Failed 2+ Lines" for CGT eligibility.
3. **[Patient-Adherence-ML](https://www.google.com/search?q=link):** Predicts if a patient will drop off during their current mapped LOT.
4. **[Net-Guard-GTN-Optimizer](https://www.google.com/search?q=link):** Calculates the financial rebates tied to specific therapy lines.

## License

Distributed under the MIT License.

