import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 200
    visible: true
    title: "Chiros"
    visibility: Window.Maximized

    RowLayout {
        anchors.fill: parent
        spacing: 0
        
        // Left tool box
        Rectangle {
            color: "#f0f0f0"
            Layout.preferredWidth: 100
            Layout.preferredHeight: 300
        }

        // Drawing area
        Rectangle {
            color: "#ffffff"
            border.color: "#cccccc"
            Layout.fillWidth: true
            Layout.fillHeight: true

            MouseArea {
                anchors.fill: parent

                onPressed: (mouse) => {
                    console.log("Mouse pressed at: " + mouse.x + ", " + mouse.y);
                }
            }
        }
    }
}