---
title: "Decision: GitHub Pages and GitHub Actions for Deployment"
date: 2025-10-17T15:45:00-07:00 # Approximate date of decision
draft: false
description: "Documenting the rationale and implementation of using GitHub Pages for hosting and GitHub Actions for automated CI/CD for the Quality Share website."
tags: ["architecture", "decision", "deployment", "github-pages", "github-actions", "ci-cd"]
related_risks: ["GitHub Actions Build/Deployment Limits"]
alternatives_considered: ["Manual deployment", "Other hosting providers (e.g., Netlify, Vercel)"]
rationale: "The decision to use GitHub Pages for hosting and GitHub Actions for Continuous Integration/Continuous Deployment (CI/CD) was driven by several key factors:
1.  **Cost-Effectiveness:** Both GitHub Pages and GitHub Actions offer generous free tiers, making them ideal for a personal project with minimal budget constraints.
2.  **Automation & Efficiency:** GitHub Actions provides a robust platform for automating the build and deployment process of the Hugo site, ensuring that every push to the main branch automatically updates the live website. This reduces manual effort and potential for errors.
3.  **Skill Showcase:** Implementing a CI/CD pipeline with GitHub Actions demonstrates proficiency in modern DevOps practices, which is valuable for showcasing technical skills.
4.  **Integration with GitHub:** Seamless integration with the project's source code repository on GitHub simplifies management and workflow.
5.  **Performance:** GitHub Pages leverages a global CDN, ensuring fast content delivery to users worldwide.

While other hosting providers offer similar services, the tight integration with GitHub and the cost-effectiveness made this the optimal choice for the project's current stage."
impact: "The deployment strategy requires a dedicated `gh-pages` branch to separate the source code from the built static assets, maintaining a clean repository history. The initial setup involved troubleshooting `baseURL` configurations and `publish_dir` settings within the GitHub Actions workflow. Potential risks related to GitHub Actions build minutes and GitHub Pages bandwidth limits were assessed as low for the current project scope."
---

## Context

Following the selection of Hugo as the Static Site Generator, a robust and automated deployment strategy was required to publish the website to a live environment. The primary goals were to ensure cost-effectiveness, automation, and high performance for the end-users.

## Alternatives Considered

*   **Manual Deployment:** Building the Hugo site locally and manually uploading the `public/` directory to a web server.
*   **Other Hosting Providers:** Services like Netlify or Vercel offer similar static site hosting and CI/CD capabilities.

## Decision

**GitHub Pages** was selected for hosting, and **GitHub Actions** was chosen for automated CI/CD.

## Rationale

The choice was based on:

*   **Cost-Effectiveness:** Leveraging the free tiers of GitHub Pages and GitHub Actions.
*   **Automation:** Establishing an automated pipeline for building and deploying the Hugo site upon every push to the `main` branch.
*   **Skill Showcase:** Demonstrating proficiency in CI/CD practices.
*   **Seamless Integration:** Utilizing the native integration within the GitHub ecosystem.
*   **Performance:** Benefiting from GitHub Pages' global CDN for fast content delivery.

## Implications & Future Considerations

This deployment strategy necessitates the use of a `gh-pages` branch for the built static assets, keeping the `main` branch clean. Initial setup involved careful configuration of the GitHub Actions workflow, particularly regarding the `baseURL` and `publish_dir` to ensure correct asset loading. The free tier limits for GitHub Actions and GitHub Pages were assessed and deemed sufficient for the project's current and foreseeable scale.
