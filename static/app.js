document.addEventListener("DOMContentLoaded", async () => {
  const container = document.getElementById("blog-container");
  const loading = document.getElementById("loading");

  try {
    const res = await fetch("/api/posts");
    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);

    const posts = await res.json();
    loading.remove(); // 移除加载提示

    posts.forEach((post) => {
      const article = document.createElement("article");
      article.className = "post";
      article.innerHTML = `
                <h2>${escapeHtml(post.title)}</h2>
                <div class="date">${post.date}</div>
                <p>${escapeHtml(post.content)}</p>
            `;
      container.appendChild(article);
    });
  } catch (err) {
    loading.textContent = `❌ 加载失败: ${err.message}`;
    loading.style.color = "#ef4444";
  }
});

// 简易防 XSS 函数
function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}
