(() => {
	"use strict";

	const lang = (document.documentElement.lang || "en_IE").toLowerCase();

	const profiles = {
		en_IE: {
			key: "en_IE",
			contactIntro: "Share your question in your own words. We will reply as clearly as possible.",
			submitIntro: "Use this form to present your work in your own voice.",
			requiredMessage: "Please complete this field.",
			emailMessage: "Please enter a valid email address.",
			otherPurposePrompt: "Add a short subject or purpose",
			confirmContact: "Send this message now?",
			confirmSubmit: "Submit your artwork for review now?",
			structuredFlow: false,
		},
		ja_JP: {
			key: "ja_JP",
			contactIntro: "\u3054\u4e0d\u660e\u70b9\u306f\u3001\u5fc5\u8981\u4e8b\u9805\u3092\u9806\u306b\u3054\u8a18\u5165\u304f\u3060\u3055\u3044\u3002",
			submitIntro: "\u5b8c\u6574\u306a\u5be9\u67fb\u306e\u305f\u3081\u3001\u9805\u76ee\u3092\u9806\u756a\u306b\u3054\u5165\u529b\u304f\u3060\u3055\u3044\u3002",
			requiredMessage: "\u3053\u306e\u9805\u76ee\u3092\u5165\u529b\u3057\u3066\u304f\u3060\u3055\u3044\u3002",
			emailMessage: "\u6709\u52b9\u306a\u30e1\u30fc\u30eb\u30a2\u30c9\u30ec\u30b9\u3092\u3054\u5165\u529b\u304f\u3060\u3055\u3044\u3002",
			otherPurposePrompt: "\u4ef6\u540d\u307e\u305f\u306f\u76ee\u7684\u3092\u7c21\u6f54\u306b\u3054\u8a18\u5165\u304f\u3060\u3055\u3044",
			confirmContact: "\u3053\u306e\u5185\u5bb9\u3092\u9001\u4fe1\u3057\u307e\u3059\u304b\uff1f",
			confirmSubmit: "\u3053\u306e\u4f5c\u54c1\u3092\u5be9\u67fb\u7528\u306b\u63d0\u51fa\u3057\u307e\u3059\u304b\uff1f",
			structuredFlow: true,
		},
		zh_CN: {
			key: "zh_CN",
			contactIntro: "\u8bf7\u6309\u987a\u5e8f\u586b\u5199\u5fc5\u586b\u5185\u5bb9\uff0c\u4ee5\u4fbf\u6211\u4eec\u5c3d\u5feb\u5904\u7406\u3002",
			submitIntro: "\u4e3a\u786e\u4fdd\u5ba1\u6838\u6548\u7387\uff0c\u8bf7\u5b8c\u6574\u586b\u5199\u4e0b\u5217\u4fe1\u606f\u3002",
			requiredMessage: "\u8bf7\u586b\u5199\u6b64\u5b57\u6bb5\u3002",
			emailMessage: "\u8bf7\u8f93\u5165\u6709\u6548\u7684\u7535\u5b50\u90ae\u7bb1\u5730\u5740\u3002",
			otherPurposePrompt: "\u8bf7\u586b\u5199\u7b80\u77ed\u4e3b\u9898\u6216\u76ee\u7684",
			confirmContact: "\u786e\u8ba4\u53d1\u9001\u6b64\u6d88\u606f\u5417\uff1f",
			confirmSubmit: "\u786e\u8ba4\u63d0\u4ea4\u6b64\u4f5c\u54c1\u4f9b\u753b\u5eca\u5ba1\u6838\u5417\uff1f",
			structuredFlow: true,
		},
	};

	function getProfile() {
		if (lang.startsWith("ja")) {
			return profiles.ja_JP;
		}
		if (lang.startsWith("zh")) {
			return profiles.zh_CN;
		}
		return profiles.en_IE;
	}

	function addFormNotice(form, text) {
		if (!form || !text || form.querySelector(".js-culture-note")) {
			return;
		}
		const note = document.createElement("div");
		note.className = "alert alert-light border js-culture-note";
		note.setAttribute("role", "status");
		note.textContent = text;
		form.prepend(note);
	}

	function applyValidationTone(form, profile) {
		if (!form) {
			return;
		}

		const requiredFields = form.querySelectorAll("input[required], textarea[required], select[required]");
		requiredFields.forEach((field) => {
			field.addEventListener("invalid", () => {
				if (field.validity.valueMissing) {
					field.setCustomValidity(profile.requiredMessage);
				} else if (field.type === "email" && field.validity.typeMismatch) {
					field.setCustomValidity(profile.emailMessage);
				}
			});

			field.addEventListener("input", () => {
				field.setCustomValidity("");
			});
		});
	}

	function applyStructuredSections(form) {
		if (!form) {
			return;
		}
		const sectionTitles = form.querySelectorAll("h5");
		sectionTitles.forEach((title, idx) => {
			if (!/^\d+\.\s/.test(title.textContent || "")) {
				title.textContent = `${idx + 1}. ${title.textContent}`;
			}
		});
	}

	function wirePurposeField(profile) {
		const purpose = document.getElementById("purpose");
		const otherPurpose = document.getElementById("other_purpose");
		if (!purpose || !otherPurpose) {
			return;
		}

		const syncOtherPurpose = () => {
			const isOther = purpose.value === "other";
			otherPurpose.required = isOther;
			otherPurpose.placeholder = profile.otherPurposePrompt;
			if (!isOther) {
				otherPurpose.setCustomValidity("");
			}
		};

		purpose.addEventListener("change", syncOtherPurpose);
		syncOtherPurpose();
	}

	function wireConfirmOnSubmit(form, message) {
		if (!form || !message) {
			return;
		}
		form.addEventListener("submit", (event) => {
			if (!window.confirm(message)) {
				event.preventDefault();
			}
		});
	}

	function wireActiveNavbarState() {
		const path = window.location.pathname.replace(/\/$/, "") || "/";
		const navLinks = document.querySelectorAll(".navbar .nav-link[href]");
		navLinks.forEach((link) => {
			const href = (link.getAttribute("href") || "").replace(/\/$/, "") || "/";
			if (href === path) {
				link.classList.add("is-active");
				link.setAttribute("aria-current", "page");
			}
		});
	}

	document.addEventListener("DOMContentLoaded", () => {
		const profile = getProfile();
		document.documentElement.setAttribute("data-culture-profile", profile.key);

		const contactForm = document.querySelector('form[action="/contact"]');
		const submitForm = document.querySelector('form[action="/submit"]');

		addFormNotice(contactForm, profile.contactIntro);
		addFormNotice(submitForm, profile.submitIntro);

		applyValidationTone(contactForm, profile);
		applyValidationTone(submitForm, profile);

		wirePurposeField(profile);
		wireConfirmOnSubmit(contactForm, profile.confirmContact);
		wireConfirmOnSubmit(submitForm, profile.confirmSubmit);
		wireActiveNavbarState();

		if (profile.structuredFlow) {
			applyStructuredSections(submitForm);
		}

		const yearInput = document.getElementById("year");
		if (yearInput) {
			yearInput.max = String(new Date().getFullYear());
		}
	});
})();
