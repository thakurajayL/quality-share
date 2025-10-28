---
title: "Architectural Decision: Single Content Model for Flexibility"
date: 2025-10-19
---

## Context

As part of defining the data models for the Quality Share project, a key decision was required on how to represent different types of content that the AI pipeline will process. The initial requirement is to handle both blog posts and research papers, with the potential for other content types (e.g., videos, books) in the future.

## Options Considered

### 1. A Single, Unified `ContentItem` Model

This approach uses a single model to represent all types of content. A `content_type` field (e.g., "BLOG_POST", "RESEARCH_PAPER") is used to differentiate between them. Fields that are specific to one type of content (e.g., `doi` for a research paper) are made optional/nullable.

### 2. Separate, Specific Models

This approach involves creating a distinct data model for each content type (e.g., a `BlogPost` model and a `ResearchPaper` model). Each model would have only the fields relevant to that specific type.

## Decision

We have decided to adopt **Option 1: A Single, Unified `ContentItem` Model**.

## Rationale

The primary driver for this decision is **flexibility and long-term scalability**. The "trusted librarian" vision for this project implies that the ability to incorporate new and varied types of content over time is a core strategic goal.

*   **Adaptability:** A single model allows us to introduce new content types (e.g., "VIDEO", "BOOK_SUMMARY") simply by adding a new value to the `content_type` enum, without requiring changes to the database schema or creating new API endpoints.
*   **Simplicity of Queries:** It is far simpler to query and manage a single collection of content items, for example, to retrieve "all content published in the last week," regardless of type.
*   **Reduced Code Duplication:** Core logic for fetching, storing, summarizing, and ranking content can be written once and applied to all content types.
*   **Alignment with Architectural Principles:** This decision directly supports our goal of a "Living Architecture" that is designed to evolve and adapt over time.

## Implications

*   The `ContentItem` data model will contain some fields that are optional/nullable to accommodate the specific attributes of different content types.
*   Application logic will need to handle these optional fields gracefully.
*   The `content_type` field becomes a critical piece of data for any logic that needs to differentiate between content types.
