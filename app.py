from flask import Flask, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "corevista-software-secret-2026"

COMPANY_INFO = {
    "legal_name": "TitanCore Computer and Hardware Systems",
    "entity_number": "Texas, USA",
    "registered": "Texas, USA",
    "registered_agent": "TitanCore Sales Team",
    "registered_office": "Texas, USA",
    "email": "sales@titancoresystems.com",
    "phone": "+1 (903) 787-3060",
    "whatsapp": "+1 (903) 787-3060",
    "business_purpose": (
        "To design, configure, and deliver high-performance GPU systems, AI training servers, "
        "enterprise workstations, and data center infrastructure for businesses, researchers, "
        "and institutions."
    ),
}

SERVICES = [
    {
        "id": "gpu-server-systems",
        "name": "GPU Server Systems",
        "icon": "fa-server",
        "description": (
            "Purpose-built AI and high-performance compute platforms with enterprise-grade "
            "GPU density, thermal efficiency, and compute headroom."
        ),
        "image": (
            "https://images.unsplash.com/photo-1518770660439-4636190af475"
            "?auto=format&fit=crop&w=1200&q=85"
        ),
        "features": [
            "Multi-GPU rack servers",
            "AI workload tuning",
            "High-density cooling",
            "Low-latency networking",
        ],
    },
    {
        "id": "ai-training-platforms",
        "name": "AI Training Platforms",
        "icon": "fa-brain",
        "description": (
            "Scalable training environments engineered for model development, research, and "
            "accelerated iteration across compute-intensive workloads."
        ),
        "image": (
            "https://images.unsplash.com/photo-1677442136019-21780ecad995"
            "?auto=format&fit=crop&w=1200&q=85"
        ),
        "features": [
            "Deep learning clusters",
            "Model training readiness",
            "Data-center scale-up",
            "Power-aware deployment",
        ],
    },
    {
        "id": "workstations-and-infrastructure",
        "name": "Workstations & Infrastructure",
        "icon": "fa-microchip",
        "description": (
            "High-performance workstation and data center solutions designed for demanding "
            "simulation, research, rendering, and production environments."
        ),
        "image": (
            "https://images.unsplash.com/photo-1498050108023-c5249f4df085"
            "?auto=format&fit=crop&w=1200&q=85"
        ),
        "features": [
            "Advanced GPU workstations",
            "Enterprise storage layouts",
            "Data center deployment",
            "Support and maintenance",
        ],
    },
]

PROCESS_STEPS = [
    {
        "number": "01",
        "title": "Consult & Scope",
        "description": (
            "We assess your workload, GPU density, and infrastructure needs to shape a build "
            "that matches your performance and budget requirements."
        ),
        "icon": "fa-compass",
    },
    {
        "number": "02",
        "title": "Design & Configure",
        "description": (
            "Our team configures the right CPU, GPU, memory, storage, and networking stack for "
            "reliable day-one performance."
        ),
        "icon": "fa-diagram-project",
    },
    {
        "number": "03",
        "title": "Build & Validate",
        "description": (
            "Every system is assembled, tested, and quality-checked to ensure thermal efficiency "
            "and compute stability before deployment."
        ),
        "icon": "fa-code-branch",
    },
    {
        "number": "04",
        "title": "Deploy & Support",
        "description": (
            "We support installation, optimization, and long-term uptime so your hardware keeps "
            "performing as your workload grows."
        ),
        "icon": "fa-cloud-arrow-up",
    },
]

WHY_CHOOSE_US = [
    {
        "title": "Texas-based expertise",
        "description": (
            "Built on practical experience serving high-demand compute environments, customer "
            "support, and performance-first engineering decisions."
        ),
        "icon": "fa-shield-halved",
    },
    {
        "title": "AI-ready infrastructure",
        "description": (
            "Solutions designed for machine learning, deep learning, simulation, rendering, and "
            "high-throughput research operations."
        ),
        "icon": "fa-brain",
    },
    {
        "title": "Custom system design",
        "description": (
            "No one-size-fits-all builds—each configuration is tuned for exactly the workload you "
            "need to run."
        ),
        "icon": "fa-circle-check",
    },
    {
        "title": "Performance that scales",
        "description": (
            "From single-GPU workstations to data center GPU clusters, we engineer systems that "
            "grow with your operations."
        ),
        "icon": "fa-handshake",
    },
]

ABOUT = (
    "TitanCore Computer and Hardware Systems is a Texas-based technology hardware company "
    "specializing in high-performance computing, AI training servers, GPU systems, enterprise "
    "workstations, and data center infrastructure. We provide reliable, cutting-edge computing "
    "solutions that empower businesses, researchers, and institutions to accelerate innovation.\n\n"
    "From AI lab deployments to enterprise compute refreshes, TitanCore helps organizations turn "
    "performance demands into dependable infrastructure. We focus on robust engineering, tailored "
    "server configurations, and support that keeps complex workloads moving without interruption."
)

KEY_SPECIFICATIONS = [
    "Support for up to 10 NVIDIA GPUs",
    "Multiple CPU options, including Intel Xeon and AMD EPYC",
    "Up to 6 TB of memory",
    "Multiple storage options, including NVMe, SATA, and SAS drives",
    "High-speed networking options, including 10/25/40/100 GbE",
]

IDEAL_USE_CASES = [
    "Deep learning and neural network training",
    "Image and speech recognition",
    "Natural language processing",
    "Robotics and autonomous vehicles",
    "Medical research and analysis",
    "Financial modeling and analysis",
]

GPU_PRODUCTS = [
    {
        "name": "SuperServer 112B-WR",
        "supports": "Intel Xeon 6",
        "cpu": "Intel Xeon 6 SP",
        "gpu": "2 PCIe 5.0 x16",
        "memory": "1 TB DDR5 ECC RDIMM",
        "storage": "8 2.5\" SATA/SAS Hot-Swap",
        "networking": "Redundant Power",
        "price": "15,733.00",
    },
    {
        "name": "SuperServer 512B-WR",
        "supports": "Intel Xeon 6",
        "cpu": "Intel Xeon 6 SP",
        "gpu": "1 PCIe 5.0 x8 LP + 2 PCIe 5.0 x16",
        "memory": "1 TB DDR5 ECC RDIMM",
        "storage": "4 3.5\" SATA/SAS Hot-Swap",
        "networking": "Redundant Power",
        "price": "15,321.00",
    },
    {
        "name": "SuperServer 522B-WR",
        "supports": "Intel Xeon 6",
        "cpu": "Intel Xeon 6 SP",
        "gpu": "2 PCIe 5.0 x8 LP + 2 PCIe 5.0 x16",
        "memory": "1 TB DDR5 ECC RDIMM",
        "storage": "8 3.5\" SATA/SAS Hot-Swap",
        "networking": "Redundant Power",
        "price": "15,726.00",
    },
    {
        "name": "SuperServer 112C-TN",
        "supports": "Intel Xeon 6",
        "cpu": "Intel Xeon 6 SP",
        "gpu": "2 PCIe 5.0 x16",
        "memory": "2 TB DDR5 ECC RDIMM",
        "storage": "8 2.5\" SATA/SAS/NVMe Hot-Swap",
        "networking": "Redundant Power",
        "price": "43,308.00",
    },
    {
        "name": "SuperServer 122C-TN",
        "supports": "Intel Xeon 6",
        "cpu": "Intel Xeon 6 SP",
        "gpu": "2 PCIe 5.0 x16 LP",
        "memory": "2 TB DDR5 ECC RDIMM",
        "storage": "4 2.5\" SATA/SAS/NVMe Hot-Swap",
        "networking": "Redundant Power",
        "price": "28,398.00",
    },
    {
        "name": "SuperServer 122H-TN",
        "supports": "Intel Xeon 6",
        "cpu": "Intel Xeon 6 SP",
        "gpu": "3 PCIe 5.0 x16",
        "memory": "8 TB DDR5 ECC RDIMM",
        "storage": "8 2.5\" NVMe Hot-Swap",
        "networking": "Redundant Power",
        "price": "27,215.00",
    },
    {
        "name": "SuperServer 421GE-TNRT",
        "supports": "Intel 5th/4th Gen Xeon Scalable",
        "cpu": "Intel 5th/4th Gen Xeon Scalable",
        "gpu": "12 PCIe 5.0 x16",
        "memory": "4 TB DDR5 ECC RDIMM",
        "storage": "8 2.5\" NVMe Hot-Swap",
        "networking": "Dual 10-Gigabit Ethernet",
        "price": "43,294.00",
    },
    {
        "name": "GPU SuperServer A22GA-NBRT",
        "supports": "Intel Xeon 6",
        "cpu": "Intel Xeon 6 AP",
        "gpu": "2 PCIe 5.0 x16",
        "memory": "3 TB DDR5 ECC RDIMM",
        "storage": "10 2.5\" NVMe Hot-Swap",
        "networking": "Dual 10-Gigabit Ethernet",
        "price": "531,325.00",
    },
]


@app.route("/")
def index():
    return render_template(
        "corevista.html",
        company=COMPANY_INFO,
        about=ABOUT,
        services=SERVICES,
        process_steps=PROCESS_STEPS,
        reasons=WHY_CHOOSE_US,
        products=GPU_PRODUCTS,
        specifications=KEY_SPECIFICATIONS,
        use_cases=IDEAL_USE_CASES,
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            return render_template(
                "contact.html",
                company=COMPANY_INFO,
                success=False,
                error="Please provide your name, email, and message.",
                form_data={
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "message": message,
                },
            ), 400

        return render_template(
            "contact.html",
            company=COMPANY_INFO,
            success=True,
            name=name,
            message=(
                "Thank you for contacting TitanCore Computer and Hardware Systems. "
                "We will be in touch soon."
            ),
        )

    return render_template(
        "contact.html",
        company=COMPANY_INFO,
        success=False,
        form_data={},
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

