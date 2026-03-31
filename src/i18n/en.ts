import type { Translations } from './types';

export const en: Translations = {
  site: {
    name: 'Detay Multimedia',
    tagline: "We don't sell technology. We sell results.",
    description:
      'Detay Multimedia — Your operational partner for end-to-end business automation. Enterprise efficiency without hiring engineers.',
  },

  nav: {
    solutions: 'Solutions',
    allSolutions: 'All Solutions →',
    services: 'Services',
    references: 'Case Studies',
    about: 'About',
    contact: 'Contact',
    cta: 'Get Demo →',
  },

  home: {
    heroLabel: 'Enterprise Business Automation',
    heroTitle: ["We automate your", 'operations.', 'No engineers needed.'],
    heroSub:
      "We identify time-consuming, repetitive processes in your company and automate them end-to-end. We don't sell technology — we sell results. Managing enterprise projects since 1997.",
    ctaPrimary: 'Request Demo →',
    ctaSecondary: 'Explore Solutions',
    statsValue1: '27',
    statsLabel1: 'Years of Experience',
    statsValue2: '65%',
    statsLabel2: 'Avg. Manual Work Reduction',
    statsValue3: '48h',
    statsLabel3: 'First Response Time',
    trustLabel: 'Experience',
    trustDesc: 'Worked with enterprise brands including Shell, Procter & Gamble, Bayer and Anadolu Group — since 1997',
    whyLabel: 'Why Automation?',
    whyTitle: 'How many of these problems exist in your company?',
    pains: [
      {
        title: 'Human Error Risk',
        desc: 'Manual data entry, copy-paste processes, information lost in email chains. Small daily errors with big consequences.',
        stat: '80% of errors occur in repetitive tasks',
      },
      {
        title: 'Processes That Cannot Scale',
        desc: "As your team grows, processes get complex. New hire = new training = new error risk. Automation systems grow as you grow.",
        stat: "67% of companies can't scale due to manual processes",
      },
      {
        title: 'Invisible Time Waste',
        desc: 'How many hours per week are spent compiling reports? Transferring data? Asking "did that email go out?"',
        stat: 'Employees spend 40% of their time on repetitive tasks',
      },
    ],
    sectorsLabel: 'Industries',
    sectorsTitle: 'Automation Tailored to Your Industry',
    sectorsSub:
      "We configure the same technology differently for different industries. A logistics company's problem is different from a law firm's — so our solution should be too.",
    sectorsMissing: "Don't see your industry?",
    sectorsMissingCta: 'Contact us →',
    processLabel: 'Process',
    processTitle: 'How We Work',
    processSub: "We're with you at every step from the first meeting to go-live.",
    steps: [
      {
        number: '01',
        title: 'Analysis',
        desc: "We listen to your processes. We identify where time is lost and which steps are being repeated.",
        duration: '1–3 days',
      },
      {
        number: '02',
        title: 'Design',
        desc: "We create a custom automation map. Which tool, which integration, which priority order.",
        duration: '3–5 days',
      },
      {
        number: '03',
        title: 'Implementation',
        desc: "We build the system, test it, and onboard your team. You just give approval.",
        duration: '1–4 weeks',
      },
      {
        number: '04',
        title: 'Optimization',
        desc: "After the system goes live, we measure and improve. Not a one-time project — an ongoing partnership.",
        duration: 'Ongoing',
      },
    ],
    referencesLabel: 'Case Studies',
    referencesTitle: 'We Let Results Speak',
    referencesAll: 'All Case Studies →',
  },

  ctaBanner: {
    label: "Let's Start",
    title: 'Ready to automate your operations?',
    subtitle: 'Book a free analysis session with a 48-hour response guarantee.',
    cta: 'Book Demo Session →',
  },

  solutionsHub: {
    label: 'Solutions',
    title: 'Automation Solutions Tailored to Your Industry',
    subtitle: 'We configure the same technology differently for different industries.',
    inspect: 'Explore →',
    noSectorTitle: "Don't see your industry?",
    noSectorSub: "We most likely have a solution. Let's talk.",
    noSectorCta: "Talk to us →",
  },

  sectorPage: {
    label: 'Automation',
    ctaDemo: 'Get Demo for This Industry →',
    problemsLabel: 'Sound familiar?',
    problemsTitle: 'Problems We See in This Industry',
    solutionLabel: 'Automation Map',
    solutionTitle: 'From Problem to Outcome',
    solutionSub: 'For every manual process, we put an automation outcome.',
    techLabel: 'Infrastructure',
    techTitle: 'We Build the System, You Use It',
    techSub: "What technology we use matters less than what results you get. But for the curious:",
    referencesLabel: 'Case Studies',
    referencesTitle: 'Cases from This Industry',
    noCaseText: "We're starting new projects in this industry.",
    noCaseCta: 'Be Our First Reference →',
    ctaSuffix: 'industry — request a custom analysis',
    ctaSubtitle: "We analyze your processes and create a custom automation roadmap. Free.",
    ctaBtn: 'Request Analysis →',
    problemCol: 'Current Problem',
    outcomeCol: 'Automation Outcome',
    problemBadge: 'Problem',
    outcomeBadge: 'Outcome',
  },

  services: {
    metaTitle: 'Services',
    metaDesc: 'Our workflow automation, data integration, reporting, and process analysis services.',
    heroLabel: 'Services',
    heroTitle: 'What We Do',
    heroSub: "We use technology as a tool. What we offer isn't technology — it's results.",
    categories: [
      {
        title: 'Process Analysis & Automation Mapping',
        desc: "We observe your existing processes and identify which ones are suitable for automation. We produce a priority order, estimated savings, and implementation plan.",
        useCases: [
          'Operations process audit',
          'Time-loss analysis',
          'Automation ROI calculation',
          'Roadmap creation',
        ],
        duration: '3–5 days',
        sectors: ['Manufacturing', 'Logistics', 'Professional Services'],
      },
      {
        title: 'Workflow Automation',
        desc: "We automate repetitive steps. Email notifications, form processing, approval flows, task assignments — without human intervention.",
        useCases: [
          'Approval & notification flows',
          'Form → CRM integration',
          'Automatic task assignment',
          'Status update notifications',
        ],
        duration: '1–2 weeks',
        sectors: ['All industries'],
      },
      {
        title: 'Data Integration & Synchronization',
        desc: "We connect data across different systems. ERP, CRM, accounting, e-commerce platforms — all talking to each other.",
        useCases: [
          'ERP ↔ CRM sync',
          'E-commerce ↔ inventory',
          'Automatic accounting transfer',
          'Multi-platform data hub',
        ],
        duration: '1–3 weeks',
        sectors: ['Retail', 'Manufacturing', 'Logistics'],
      },
      {
        title: 'Reporting & Decision Support Systems',
        desc: "We turn scattered data into automated reports. Daily operations summary every morning, weekly performance dashboard — no manual compilation.",
        useCases: [
          'Automated weekly/monthly reports',
          'Executive dashboard',
          'Anomaly alert system',
          'KPI tracking panel',
        ],
        duration: '1–2 weeks',
        sectors: ['All industries'],
      },
      {
        title: 'Communication & Customer Process Automation',
        desc: "We automate manual steps in customer communication. Welcome messages, follow-up emails, survey sending, appointment reminders.",
        useCases: [
          'Customer onboarding flow',
          'Automated follow-up email',
          'Appointment reminders',
          'NPS & survey automation',
        ],
        duration: '3–7 days',
        sectors: ['Healthcare', 'Real Estate', 'Hospitality'],
      },
      {
        title: 'Continuous Optimization & Support',
        desc: "We don't walk away after building the system. Monthly review, performance measurement, improvement suggestions, and technical support.",
        useCases: [
          'Monthly system review',
          'Performance reporting',
          'Adding new processes',
          'Technical support & maintenance',
        ],
        duration: 'Ongoing',
        sectors: ['All industries'],
      },
    ],
  },

  references: {
    metaTitle: 'Case Studies',
    metaDesc: 'Detay Multimedia client case studies and success stories.',
    heroLabel: 'Case Studies',
    heroTitle: 'We Let Results Speak',
    heroSub: 'Every case is the solution to a real problem at a real company.',
    statsBar: '8 industries · Dozens of projects · Average 65% reduction in manual work',
    readMore: 'Read More →',
    emptyCta: 'Become Our Reference →',
  },

  about: {
    metaTitle: 'About Us',
    metaDesc: 'About Detay Multimedia — who we are, what we do, why we are different.',
    heroLabel: 'About Us',
    heroTitle: "We're Your Operational Partner",
    heroSub:
      "We're not an agency that sells technology. We're an operational partner that identifies time-consuming, repetitive processes in your company and automates them end-to-end.",
    missionLabel: 'Mission',
    missionTitle: 'Why We Exist',
    missionText:
      "The budgets enterprise companies spend on automation projects should also be accessible to growing companies. To make this possible, we built a team that knows the industry, understands the business language, and uses technology as a tool.",
    valuesLabel: 'Values',
    values: [
      {
        title: 'Results First',
        desc: "What technology we use matters less than what our client gains. Every project starts with measurable outcomes.",
      },
      {
        title: 'Industry Language',
        desc: "We speak logistics with logistics companies, legal language with law firms. No jargon — just business talk.",
      },
      {
        title: 'Ongoing Partnership',
        desc: "We don't deliver the project and leave. We're with you as the system grows and as the company grows.",
      },
      {
        title: 'Simplicity',
        desc: "Complex solutions are hard to maintain and hard to learn. The best automation is the one your team actually adopts.",
      },
    ],
  },

  contact: {
    metaTitle: 'Contact & Demo Request',
    metaDesc: 'Contact Detay Multimedia. 48-hour response guarantee.',
    heroLabel: 'Demo Request',
    heroTitle: "Let's Evaluate Your Processes Together",
    heroSub: "Let's discuss which processes in your company we can automate in a 30-minute call.",
    formName: 'Full Name',
    formCompany: 'Company Name',
    formSector: 'Industry',
    formSize: 'Company Size',
    formProcess: 'Process Where You Lose the Most Time',
    formProcessPlaceholder:
      "E.g.: We manually enter weekly sales reports into Excel every week...",
    formPhone: 'Phone or Email',
    formSubmit: 'Submit — We\'ll respond within 48h',
    formSuccess: '✓ Your request has been received. We will get back to you within 48 hours.',
    sizes: ['1–10', '10–50', '50–200', '200+'],
    responseNote: '48-hour response guarantee',
  },

  footer: {
    solutionsCol: 'Solutions',
    companyCol: 'Company',
    contactCol: 'Contact',
    tagline: "We don't sell technology. We sell results.\nEnterprise efficiency without engineers.",
    blog: 'Blog',
    kvkk: 'KVKK',
    privacy: 'Privacy Policy',
    terms: 'Terms of Service',
    rights: 'All rights reserved.',
  },

  sectors: [
    {
      slug: 'uretim',
      name: 'Manufacturing & Supply',
      icon: '⬡',
      summary: 'Automate production planning, inventory management and supplier communication.',
      headline: 'How many hours per day does your production line spend on paperwork?',
      subline:
        "We automate order tracking, stock alerts, supplier notifications, and production reports. Your team focuses on making things.",
      problems: [
        'Are stock levels still tracked manually?',
        'Are suppliers notified of order status via email?',
        'Is the production plan kept in Excel?',
        'Are quality control records on paper forms?',
        'Does preparing the weekly production report take 2+ hours?',
      ],
      solutions: [
        { problem: 'Manual stock tracking', outcome: 'Automatic stock alert and replenishment trigger' },
        { problem: 'Supplier email notifications', outcome: 'System-based automatic order notification' },
        { problem: 'Excel production plan', outcome: 'Real-time production dashboard' },
        { problem: 'Manual reporting', outcome: 'Weekly automatic production summary report' },
      ],
      metaDescription:
        'Business automation for manufacturing and supply chain. Automate inventory tracking, supplier notifications, and production reporting.',
    },
    {
      slug: 'lojistik',
      name: 'Logistics & Transport',
      icon: '◈',
      summary: 'Automate shipment tracking, customer notifications and driver reports.',
      headline: 'Are you still tracking shipments by phone?',
      subline:
        "The system sends notifications before customers call asking 'where is my order?' Your operations team plans instead of answering calls.",
      problems: [
        'Do customers call you to ask about shipment status?',
        'Are driver reports collected at the end of the day?',
        'Are delay notifications done manually?',
        'Is vehicle tracking data entered manually into the system?',
        'Is invoicing waiting for delivery confirmation?',
      ],
      solutions: [
        { problem: 'Customer phone inquiries', outcome: 'Automatic shipment status notifications (SMS/email)' },
        { problem: 'Manual driver reporting', outcome: 'Real-time updates via mobile app' },
        { problem: 'Delay notifications', outcome: 'Automatic alert and notification when threshold is exceeded' },
        { problem: 'Manual invoicing', outcome: 'Automatic invoice generation after delivery confirmation' },
      ],
      metaDescription:
        'Process automation for logistics and transport. Automate shipment tracking, customer notifications, and reporting.',
    },
    {
      slug: 'hukuk',
      name: 'Legal & Consulting',
      icon: '◻',
      summary: 'Streamline contract management, client tracking, and document processes.',
      headline: 'How many different tools do you use for client management?',
      subline:
        "We bring contract deadlines, client reminders, and document flow together in one automated system.",
      problems: [
        'Are contract deadlines tracked in a calendar?',
        'Are client appointment reminders sent manually?',
        'Are case documents accessed through email chains?',
        'Is invoice tracking in a separate system?',
        'Is the new client onboarding process standardized?',
      ],
      solutions: [
        { problem: 'Manual calendar tracking', outcome: 'Automatic deadline alert and reminder flow' },
        { problem: 'Manual appointment reminders', outcome: 'Automatic SMS/email reminder system' },
        { problem: 'Scattered document management', outcome: 'Centralized document archive and access automation' },
        { problem: 'Manual onboarding', outcome: 'Standard client welcome and document collection flow' },
      ],
      metaDescription:
        'Process automation for law firms and consulting companies. Automate contract tracking, client management, and document flow.',
    },
    {
      slug: 'perakende',
      name: 'Retail & E-Commerce',
      icon: '◇',
      summary: 'Integrate order, inventory, and customer service processes.',
      headline: 'How many systems do you switch between for order management?',
      subline:
        "E-commerce platform, inventory system, and accounting all talk to each other. An order comes in, the system takes action.",
      problems: [
        'Is inventory updated manually across multiple platforms?',
        'Are return processes managed via email chain?',
        'Are customer questions collected in one place?',
        'Are shipping notifications sent automatically?',
        'Are sales reports compiled from multiple sources?',
      ],
      solutions: [
        { problem: 'Multi-platform inventory management', outcome: 'Centralized inventory sync (real-time)' },
        { problem: 'Manual return process', outcome: 'Automatic return approval and flow' },
        { problem: 'Scattered customer inquiries', outcome: 'Unified customer communication center' },
        { problem: 'Manual sales reporting', outcome: 'Daily/weekly automatic sales summary' },
      ],
      metaDescription:
        'Process automation for retail and e-commerce. Automate inventory sync, order management, and reporting.',
    },
    {
      slug: 'saglik',
      name: 'Healthcare & Clinics',
      icon: '○',
      summary: 'Automate patient appointments, reminders, and reporting.',
      headline: 'Are appointment reminders still being made by the secretary?',
      subline:
        "We automate patient communication, appointment management, and clinic reporting. Your team focuses on patients.",
      problems: [
        'Are appointment reminders called manually?',
        'Is your no-show rate high?',
        'Does accessing patient files take time?',
        'Are insurance and billing processes manual?',
        'How are periodic check-up invitations sent?',
      ],
      solutions: [
        { problem: 'Manual appointment reminders', outcome: 'Automatic SMS/WhatsApp reminder (24h and 2h before)' },
        { problem: 'High no-show rate', outcome: 'Occupancy optimization with reminder + confirmation system' },
        { problem: 'Manual insurance processing', outcome: 'Insurance form automation and tracking system' },
        { problem: 'Periodic check-up tracking', outcome: 'Automatic patient recall campaign' },
      ],
      metaDescription:
        'Process automation for clinics and healthcare institutions. Automate appointment management, patient communication, and reporting.',
    },
    {
      slug: 'gayrimenkul',
      name: 'Real Estate & Construction',
      icon: '▣',
      summary: 'Streamline portfolio management, client tracking and contract processes.',
      headline: 'Which system do you use to track every listing in your portfolio?',
      subline:
        "We bring client inquiries, listing management, and contract processes into one single flow.",
      problems: [
        'Are incoming inquiry form queries collected in one place?',
        'Are listing updates done manually on multiple platforms?',
        'Should client follow-up emails be personalized but no time for it?',
        'Are rent/installment reminders done manually?',
        'Does the contract process involve gathering documents?',
      ],
      solutions: [
        { problem: 'Scattered client inquiries', outcome: 'Centralized inquiry collection and automatic routing' },
        { problem: 'Multi-platform listing management', outcome: 'Single-point multi-platform listing sync' },
        { problem: 'Manual rent reminders', outcome: 'Automatic rent reminder and late payment notification' },
        { problem: 'Manual contract tracking', outcome: 'Contract deadline alert and renewal flow' },
      ],
      metaDescription:
        'Process automation for real estate and construction. Automate portfolio management, client tracking, and contract processes.',
    },
    {
      slug: 'konaklama',
      name: 'Hospitality',
      icon: '▨',
      summary: 'Automate reservations, guest communication and operations reports.',
      headline: 'How many emails are written to reach guests before check-in?',
      subline:
        "We automate the guest welcome flow, reservation notifications, and operations reporting.",
      problems: [
        'Are reservation confirmations and reminders sent manually?',
        'Is the pre-guest information form collected via email?',
        'Are reservations from different channels in one place?',
        'Are operations reports prepared manually for the morning meeting?',
        'How are post-stay review requests sent?',
      ],
      solutions: [
        { problem: 'Manual reservation notifications', outcome: 'Automatic confirmation, reminder, and welcome flow' },
        { problem: 'Scattered channel management', outcome: 'Centralized reservation management system' },
        { problem: 'Manual morning report', outcome: 'Daily automatic occupancy and operations summary' },
        { problem: 'Manual review request', outcome: 'Automatic review collection flow after check-out' },
      ],
      metaDescription:
        'Process automation for hotels and hospitality facilities. Automate reservation management, guest communication, and reporting.',
    },
    {
      slug: 'egitim',
      name: 'Education & Institutions',
      icon: '▦',
      summary: 'Digitize student enrollment, notifications and reporting processes.',
      headline: 'How many people process enrollment forms manually during registration season?',
      subline:
        "We automate the entire student enrollment flow, notifications, and institutional reporting.",
      problems: [
        'Are enrollment forms collected via email or paper?',
        'Are payment reminders sent manually?',
        'Are parent notifications personalized but time-consuming?',
        'Are exam and schedule changes announced via SMS/email?',
        'Are end-of-term reports prepared manually?',
      ],
      solutions: [
        { problem: 'Manual enrollment form processing', outcome: 'Automatic enrollment flow and confirmation notification' },
        { problem: 'Manual payment reminders', outcome: 'Automatic payment reminder and late notification' },
        { problem: 'Bulk parent notifications', outcome: 'Segmented automatic notification system' },
        { problem: 'Manual term report', outcome: 'Automatic end-of-term performance report' },
      ],
      metaDescription:
        'Process automation for educational institutions. Automate student enrollment management, parent notifications, and reporting.',
    },
  ],
};
