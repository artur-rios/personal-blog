function changeToLocalization(localizationCode) {
  if (!isLocalizationCodeValid(localizationCode)) {
    return;
  }

  const currentUrl = window.location.href.replace(/^https?:\/\//, "");
  const urlProtocol = "https://";

  const localizations = [
    { code: "en", domain: "www.techcraftsman.blog" },
    { code: "pt", domain: "pt.techcraftsman.blog" },
  ];

  const localizationDomain = localizations.find(
    (domain) => domain.code === localizationCode
  ).domain;

  const urlFragments = currentUrl.split("/");

  if (urlFragments[0] === localizationDomain) {
    return;
  }

  urlFragments[0] = localizationDomain;

  const newUrl = urlFragments.join("/");

  window.location.href = `${urlProtocol}${newUrl}`;
}

function isLocalizationCodeValid(localizationCode) {
  let validLocalizationCodes = ["en", "pt"];

  if (typeof localizationCode !== "string") {
    return false;
  }

  return validLocalizationCodes.includes(localizationCode);
}
