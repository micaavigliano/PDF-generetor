from fpdf import FPDF

def clean_text(text):
    return (
        text.replace("–", "-")
        .replace("—", "-")
        .replace("•", "-")
        .encode("latin-1", "ignore")
        .decode("latin-1")
    )

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Helvetica", size=11)

def section_title(title):
    pdf.set_font("Helvetica", "B", 12)
    pdf.ln(6)
    pdf.cell(0, 10, clean_text(title), ln=True)
    pdf.set_font("Helvetica", size=11)

# Header
pdf.set_font("Helvetica", "B", 16)
pdf.cell(0, 10, clean_text("Micaela Avigliano - Frontend Developer & Accessibility Analyst"), ln=True, align="C")
pdf.set_font("Helvetica", size=11)
pdf.ln(4)
pdf.multi_cell(0, 8, clean_text("micaela.avigliano@gmail.com\nWebsite: micaavigliano.com - GitHub: github.com/micaavigliano"))

# About Me
section_title("About Me")
about_text = """Senior Frontend Engineer with 6+ years of experience building inclusive, scalable, and high-performance web applications. Specialized in React, Next.js, TypeScript, and accessibility (WCAG, ARIA). Contributed to major platforms across finance, e-commerce, streaming, and agriculture, working with global teams across 28+ countries."""
pdf.multi_cell(0, 8, clean_text(about_text))

# Tech Summary
section_title("Tech Summary")
tech_text = """- Languages & Frameworks: JavaScript, TypeScript, HTML5, CSS3, React, Vue.js, Redux,
GraphQL, Next.js, Node.js, PHP
- Testing & QA: React Testing Library, Jest, Cypress, Enzyme, Axe, Lighthouse
- Accessibility: WCAG 2.1 AA, ARIA, Screen Readers (NVDA, JAWS, VoiceOver), Keyboard
Navigation
- Tools & CMS: Git, GitLab, Bitbucket, Contentful, WordPress, Drupal, Mixpanel,
Optimizely
- Styling: Tailwind, Sass, Emotion, Styled Components, Material UI, Vuetify
- Other: Agile / SCRUM, Jira, Confluence, Vercel, Webpack, Babel
- OS: Linux, macOS, Windows"""
pdf.multi_cell(0, 8, clean_text(tech_text))

# Professional Experience
section_title("Professional Experience")
jobs = [
    ("Freelance - Frontend Developer & Accessibility Analyst (Sep 2024 - Present)",
     "Worked with Nespresso, Harley-Davidson, BiomeMakers, and Supra delivering performant, accessible frontend features across international markets.\n"
     "- Built accessible components using React, Next.JS, TypeScript, Vanilla JS, Tailwind\n"
     "- Led audits (axe, VoiceOver) and implemented WCAG-compliant patterns\n"
     "- Worked with Drupal, Contentful, and microfrontend architectures\n"
     "- Deployed projects with Vercel, contributed to UI, marketing, and PDF reporting dashboards"
    ),
    ("SmartAsset - Software Engineer (Jan 2024 - Oct 2024)",
     "Led a full migration from legacy to modern stack in a fintech platform, improving SEO, maintainability, and performance.\n"
     "- Migrated systems to Next.js, React, GraphQL, PHP, WordPress\n"
     "- Improved Core Web Vitals (SSR), implemented Optimizely for A/B testing\n"
     "- Built content tools, filters, and forms; improved Lighthouse accessibility scores\n"
     "Agile collaboration with design, QA, and product teams"
    ),
    ("Ceres Imaging - Frontend Developer (Jan 2023 - Aug 2023)",
     "Developed geospatial dashboards and UI tools for growers in North/South America and Europe.\n"
     "- Migrated dashboards from Django to Next.js + GraphQL"
     "- Built filters, tables, and Mapbox layers using Vue, MUI, and React\n"
     "Fixed critical geolocation bugs and improved UI responsiveness\n"
     "Used Vercel, Recoil, and GitHub in Agile SCRUM teams"
    ),
    ("Indeed - Frontend Developer & Accessibility Analyst (Sept 2021 - Jan 2023)",
     "Focused on reusable components and accessibility within large-scale platforms.\n"
     "- Built accessible components with React, Redux, Emotion\n"
     "- Boosted test coverage to 85% using React Testing Library\n"
     "Led custom focus handling for keyboard users; refactored legacy code\n"
     "Ensured WCAG 2.1 AA and ARIA compliance; used Cypress, Storybook"
    ),
    ("Telecom - Frontend Developer (Nov 2020 - Sept 2021)",
     "Improved performance and UX on a Smart TV app during high-traffic periods.\n"
     "- Migrated app to Next.js + TypeScript, built custom spatial navigation\n"
     "- Built queue system, video player, and legacy-to-modern transition\n"
     "Used Tailwind, Storybook, and React Context"
    ),
    ("eSSENTIAL Accessibility - Accessibility Analyst (Dec 2019 - Aug 2929)",
     "Performed accessibility audits and technical remediation for major global brands in finance, retail, and food sectors.\n"
     "- Conducted WCAG 2.1 AA evaluations using axe, NVDA, JAWS, and VoiceOver\n"
     "- Fixed accessibility issues using HTML, CSS, JavaScript, React\n"
     "- Delivered compliance reports and a11y action plans\n"
     "- Mentored junior testers and collaborated across SCRUM teams\n"
    ),
    ("Accenture Argentina - Software Engineer (Jun 2019 - Dec 2019)",
     "Developed responsive web interfaces and improved accessibility in enterprise applications.\n"
     "- Built native website using Vue.js, Node.js, AWS, HTML/CSS\n"
     "- Refactored UI components for better accessibility and responsiveness\n"
    )
]
for title, content in jobs:
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 8, clean_text(title), ln=True)
    pdf.set_font("Helvetica", size=11)
    pdf.multi_cell(0, 8, clean_text(content))

section_title("Languages")
pdf.multi_cell(0, 8, clean_text("- Spanish: Native\n- English: Fluent\n- Italian: Intermediate"))

# You can change the name file to whatever you want
pdf.output("micaela-avigliano-frontend.pdf")
