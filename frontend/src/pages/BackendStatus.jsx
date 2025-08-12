import React, { useEffect, useState } from "react";

export default function BackendStatus() {
  const [status, setStatus] = useState("A verificar...");
  const [isOnline, setIsOnline] = useState(null);

  useEffect(() => {
    fetch("/health")
      .then((res) => {
        if (!res.ok) throw new Error("Resposta inválida do backend");
        return res.json();
      })
      .then((data) => {
        setStatus(`Backend online — ${new Date(data.timestamp).toLocaleString()}`);
        setIsOnline(true);
      })
      .catch(() => {
        setStatus("Backend offline");
        setIsOnline(false);
      });
  }, []);

  const cardStyle = {
    width: "400px",
    margin: "80px auto",
    padding: "30px",
    borderRadius: "12px",
    boxShadow: "0 4px 12px rgba(0,0,0,0.15)",
    textAlign: "center",
    fontSize: "1.2rem",
    background: isOnline === null ? "#f9f9f9" : isOnline ? "#e6ffed" : "#ffe6e6",
    color: isOnline === null ? "#555" : isOnline ? "#0a6400" : "#a60000",
    transition: "all 0.3s ease"
  };

  const iconStyle = {
    fontSize: "3rem",
    marginBottom: "10px"
  };

  return (
    <div style={cardStyle}>
      <div style={iconStyle}>
        {isOnline === null ? "⏳" : isOnline ? "✅" : "❌"}
      </div>
      <div>{status}</div>
    </div>
  );
}
